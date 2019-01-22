import json
import random

import numpy as np
from copy import deepcopy

from fever.scorer import fever_score, is_correct_label, evidence_macro_recall
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import  LogisticRegression
from sklearn.metrics import classification_report

import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
from sklearn.svm import SVC
from tqdm import tqdm

random.seed(123)
np.random.seed(123)

nlp = spacy.load('en_core_web_sm')



train_actual = []

with open("data/fever-data/dev.jsonl") as file:
    for line in file:
        train_actual.append(json.loads(line))

test_actual = []

with open("data/fever-data/test.jsonl") as file:
    for line in file:
        test_actual.append(json.loads(line))


evaluate_instances = []
all_instances = []


def load_predictions(data,file):
    predictions = []

    evaluate_instances = []
    all_instances = []

    with open(file) as file:
        for line in file:
            predictions.append(json.loads(line))

    for idx, instance in enumerate(data):
        instance = deepcopy(instance)

        instance["predicted_label"] = predictions[idx]["predicted_label"]
        instance["predicted_evidence"] = predictions[idx]["predicted_evidence"]

        all_instances.append(instance)

        if evidence_macro_recall(instance)[0] < evidence_macro_recall(instance)[1]:
            evaluate_instances.append(instance)
            pass

        if is_correct_label(instance):
            #print("Correct label")
            pass
        else:
            if evidence_macro_recall(instance)[0] >= 1.0 or \
                instance["label"] == "NOT ENOUGH INFO":
                pass
                #evaluate_instances.append(instance)

    return evaluate_instances , all_instances

train_positive = []
train_s_positive = []
train_r_positive = []
train_n_positive = []
train_all = []

test_positive = []
test_s_positive = []
test_r_positive = []
test_n_positive = []
test_all = []


a,b = load_predictions(train_actual,"data/predictions/dev.jsonl")
train_positive.extend(a)
train_s_positive.extend(filter(lambda instance: instance["label"] == "SUPPORTS", a))
train_r_positive.extend(filter(lambda instance: instance["label"] == "REFUTES", a))
train_n_positive.extend(filter(lambda instance: instance["label"] == "NOT ENOUGH INFO", a))
train_all.extend(b)

a,b = load_predictions(test_actual, "data/predictions/test.jsonl")
test_positive.extend(a)
test_s_positive.extend(filter(lambda instance: instance["label"] == "SUPPORTS", a))
test_r_positive.extend(filter(lambda instance: instance["label"] == "REFUTES", a))
test_n_positive.extend(filter(lambda instance: instance["label"] == "NOT ENOUGH INFO", a))
test_all.extend(b)

def sample_negative(positive_data, exclude_data, all_data):
    ids = {i: 1 for i in (map(lambda instance: instance["id"], exclude_data))}.keys()
    sample_pool = list(filter(lambda instance: instance["id"] not in ids, all_data))

    sampled_ids = np.random.choice(len(sample_pool), size=len(positive_data), replace=False)
    negative_data = list(map(lambda id: sample_pool[id], sampled_ids))

    all_labels = [1] * len(positive_data) + [0] * len(negative_data)
    all_data = positive_data + negative_data

    train_mixed = list(zip(all_data,all_labels))
    random.shuffle(train_mixed)

    return zip(*train_mixed)

train_data, train_labels = sample_negative(train_positive,train_positive, train_all)
train_s_data, train_s_labels = sample_negative(train_s_positive, train_positive, train_all)
train_r_data, train_r_labels = sample_negative(train_r_positive, train_positive, train_all)


test_data, test_labels = sample_negative(test_positive, test_positive, test_all)
test_s_data, test_s_labels = sample_negative(test_s_positive, test_positive, test_all)
test_r_data, test_r_labels = sample_negative(test_r_positive, test_positive, test_all)


vec = CountVectorizer(ngram_range=(1,2))
vec.fit(map(lambda instance: instance["claim"], train_data))

train_Xs = vec.transform(map(lambda instance: instance["claim"], train_data))
train_ys = train_labels

train_s_Xs = vec.transform(map(lambda instance: instance["claim"], train_s_data))
train_s_ys = train_s_labels

train_r_Xs = vec.transform(map(lambda instance: instance["claim"], train_r_data))
train_r_ys = train_r_labels


valid_Xs = vec.transform(map(lambda instance: instance["claim"], test_data))
valid_ys = test_labels

valid_s_Xs = vec.transform(map(lambda instance: instance["claim"], test_s_data))
valid_s_ys = test_s_labels

valid_r_Xs = vec.transform(map(lambda instance: instance["claim"], test_r_data))
valid_r_ys = test_r_labels


lr_s = LogisticRegression(random_state=123,penalty='l2')
lr_s.fit(train_s_Xs,train_s_ys)
lr_r = LogisticRegression(random_state=123,penalty='l2')
lr_r.fit(train_r_Xs,train_r_ys)


if len(train_n_positive):
    train_n_data, train_n_labels = sample_negative(train_n_positive, train_positive, train_all)
    test_n_data, test_n_labels = sample_negative(test_n_positive, test_positive, test_all)
    train_n_Xs = vec.transform(map(lambda instance: instance["claim"], train_n_data))
    train_n_ys = train_n_labels
    valid_n_Xs = vec.transform(map(lambda instance: instance["claim"], test_n_data))
    valid_n_ys = test_n_labels
    lr_n = LogisticRegression(random_state=123,penalty='l2')
    lr_n.fit(train_n_Xs,train_n_ys)
    predicted_ys = lr_s.predict(valid_n_Xs)
    print("Score NEI: ",lr_n.score(valid_n_Xs, valid_n_ys))


predicted_ys = lr_s.predict(valid_s_Xs)
print("Score Supports: ",lr_s.score(valid_s_Xs, valid_s_ys))
predicted_ys = lr_r.predict(valid_r_Xs)
print("Score Refutes: ",lr_s.score(valid_r_Xs, valid_r_ys))


features = vec.get_feature_names()
scores = {}
for idx,weight in enumerate(lr_s.coef_[0]):
    scores[features[idx]] = weight

sorted_scores = sorted(scores.items(), key= lambda item: item[1])

print(sorted_scores[:20])
print(sorted_scores[-20:])

scores = {}
for idx,weight in enumerate(lr_r.coef_[0]):
    scores[features[idx]] = weight

sorted_scores = sorted(scores.items(), key= lambda item: item[1])

print(sorted_scores[:20])
print(sorted_scores[-20:])


if len(train_n_positive):
    scores = {}
    for idx,weight in enumerate(lr_n.coef_[0]):
        scores[features[idx]] = weight

    sorted_scores = sorted(scores.items(), key= lambda item: item[1])

    print(sorted_scores[:20])
    print(sorted_scores[-20:])

#maximum = max(scores, key=scores.get)  # Just use 'min' instead of 'max' for minimum.
#print(maximum, scores[maximum])


