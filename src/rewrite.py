import json
import re

import nltk


def tokenize(sentences):
    for sent in nltk.sent_tokenize(sentences.lower()):
        for word in nltk.word_tokenize(sent):
            yield word


all_text = ""

with open("data/paper.dev.p5.s5.jsonl") as f, \
        open("data/before.hypothesis.is.a.dev.p5.s5.jsonl","w+") as f_out_original, \
        open("data/after.hypothesis.is.a.dev.p5.s5.jsonl","w+") as f_out_changed:


    for line in f:
        line = json.loads(line)
        print(line["claim"])
        all_text += line["claim"] + " "
        matches = re.match(r"(.+) is a (.+)", line["claim"])
        if matches is not None:
            new_claim = "There exists a {0} called {1}.".format(matches.group(2).replace(".",""),matches.group(1))
            print(new_claim)
            f_out_original.write(json.dumps(line)+"\n")
            line["claim"] = new_claim
            f_out_changed.write(json.dumps(line)+"\n")




    text = nltk.Text(tokenize(all_text))
    text.collocations(num=200, window_size=4)
    print([" ".join(el) for el in text._collocations])
