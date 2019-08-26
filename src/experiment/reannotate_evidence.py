import argparse
import json
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("--in-file",type=str)
parser.add_argument("--dev-master",type=str)
parser.add_argument("--test-master",type=str)
parser.add_argument("--out-file",type=str)

args = parser.parse_args()

claims = []
dev_master = []
test_master = []
evidence = defaultdict(set)

with open(args.in_file,"r") as infile:
    for idx,line in enumerate(infile):
        line = json.loads(line)
        claims.append(line)


with open(args.dev_master,"r") as infile:
    for idx,line in enumerate(infile):
        line = json.loads(line)
        dev_master.append(line)


        for evidence_group in line["evidence"]:
            for evidence_annotation in evidence_group:
                evidence[evidence_annotation[0]].add(idx)

with open(args.test_master,"r") as infile:
    for idx,line in enumerate(infile):
        line = json.loads(line)
        test_master.append(line)


for claim in claims:
    candidate_idx = set()
    for evidence_group in claim["evidence"]:
        for evidence_annotation in evidence_group:
            candidate_idx.update(evidence[evidence_annotation[0]])

    assert len(candidate_idx)==1

    for candidate in candidate_idx:
        claim["evidence"] = test_master[candidate]["evidence"]
        claim["label"] = test_master[candidate]["label"]

    print(claim)

