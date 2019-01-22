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
train_all = []

test_positive = []
test_all = []


a,b = load_predictions(train_actual,"data/predictions/dev.jsonl")
train_positive.extend(a)
train_all.extend(b)

a,b = load_predictions(test_actual, "data/predictions/test.jsonl")
test_positive.extend(a)
test_all.extend(b)

train_claim_ids = {i:1 for i in (map(lambda instance: instance["id"], train_positive))}.keys()
train_sample_pool = list(filter(lambda instance: instance["id"] not in train_claim_ids, train_all))

train_sample_ids = np.random.choice(len(train_sample_pool), size=len(train_positive), replace=False)
train_negative = list(map(lambda id: train_sample_pool[id], train_sample_ids))


all_train_labels = [1] * len(train_positive) + [0] * len(train_negative)
all_train_data = train_positive+train_negative


test_claim_ids = {i:1 for i in (map(lambda instance: instance["id"], test_positive))}.keys()
test_sample_pool = list(filter(lambda instance: instance["id"] not in test_claim_ids, test_all))

sample_ids = np.random.choice(len(test_sample_pool), size=len(test_positive), replace=False)
train_negative = list(map(lambda id: test_sample_pool[id], sample_ids))

all_test_labels = [1] * len(train_positive) + [0] * len(train_negative)
all_test_data = train_positive+train_negative


train_mixed = list(zip(all_train_data,all_train_labels))
random.shuffle(train_mixed)

all_train_data, all_train_labels = zip(*train_mixed)

#for item in tqdm(all_train_data):
#    item["claim"] += " ".join(["ner="+str(ent.label_) for ent in nlp(item['claim']).ents])

vec = CountVectorizer(ngram_range=(1,2),min_df=10)



train_Xs = vec.fit_transform(map(lambda instance: instance["claim"], all_train_data))
train_ys = all_train_labels

valid_Xs = vec.transform(map(lambda instance: instance["claim"], all_test_data))
valid_ys = all_test_labels

lr = LogisticRegression(random_state=123,penalty='l2')
lr.fit(train_Xs,train_ys)

predicted_ys = lr.predict(valid_Xs)
print("Score: ",lr.score(valid_Xs, valid_ys))

features = vec.get_feature_names()
scores = {}
for idx,weight in enumerate(lr.coef_[0]):
    scores[features[idx]] = weight

sorted_scores = sorted(scores.items(), key= lambda item: item[1])

print(sorted_scores[:20])
print(sorted_scores[-20:])

#maximum = max(scores, key=scores.get)  # Just use 'min' instead of 'max' for minimum.
#print(maximum, scores[maximum])


