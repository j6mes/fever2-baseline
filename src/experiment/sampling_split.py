from collections import defaultdict

import numpy as np
import json
import argparse

np.random.seed(123)

parser = argparse.ArgumentParser()
parser.add_argument("--in-file",type=str)
parser.add_argument("--dev-file",type=str)
parser.add_argument("--test-file",type=str)


args = parser.parse_args()

everything = []

claims = defaultdict(list)

with open(args.in_file,"r") as infile:
    for line in infile:
        line = json.loads(line)
        claims[line["label"]].append(line)
        everything.append(line)


dev = dict()
for k in claims.keys():
    dev[k] = np.random.choice(claims[k], len(claims[k])//2, replace=False)


dev_claims = []
for v in dev.values():
    dev_claims.extend(v)

test_claims = []
for v in everything:
    if v not in dev_claims:
        test_claims.append(v)


np.random.shuffle(dev_claims)
np.random.shuffle(test_claims)

with open(args.dev_file,"w+") as outfile:
    for id,line in enumerate(dev_claims):
        line['id'] = id
        outfile.write(json.dumps(line)+"\n")

with open(args.test_file, "w+") as outfile:
    for id, line in enumerate(test_claims):
        line['id'] = id
        outfile.write(json.dumps(line) + "\n")