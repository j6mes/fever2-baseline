from collections import defaultdict

import numpy as np
import json
import argparse

np.random.seed(123)

parser = argparse.ArgumentParser()
parser.add_argument("--in-file",type=str)
parser.add_argument("--out-file",type=str)

parser.add_argument("--in-predictions-file",type=str)
parser.add_argument("--out-predictions-file",type=str)

parser.add_argument("--size",type=int)

args = parser.parse_args()


claims = defaultdict(list)
read_order = []
with open(args.in_file,"r") as infile:
    for line in infile:
        line = json.loads(line)
        read_order.append(line["id"])
        claims[line["label"]].append(line)

predictions = []
with open(args.in_predictions_file,"r") as infile:
    for idx,line in enumerate(infile):
        line = json.loads(line)
        predictions.append(line)

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


with open(args.out_predictions_file,"w+") as outfile:
    for id,line in enumerate(all_claims):
        outfile.write(json.dumps(predictions[read_order.index(line["id"])])+"\n")