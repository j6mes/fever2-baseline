from collections import defaultdict

import numpy as np
import json
import argparse

np.random.seed(123)

parser = argparse.ArgumentParser()
parser.add_argument("--in-file",type=str)
parser.add_argument("--out-file",type=str)
parser.add_argument("--size",type=int)

args = parser.parse_args()


claims = defaultdict(list)

with open(args.in_file,"r") as infile:
    for line in infile:
        line = json.loads(line)
        claims[line["label"]].append(line)


sampled = dict()
for k in claims.keys():
    sampled[k] = np.random.choice(claims[k], args.size//3, replace=False)


all_claims = []
for v in sampled.values():
    all_claims.extend(v)


np.random.shuffle(all_claims)

with open(args.out_file,"w+") as outfile:
    for id,line in enumerate(all_claims):
        line['id'] = id
        outfile.write(json.dumps(line)+"\n")