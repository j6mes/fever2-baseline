import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument("--in-file")
parser.add_argument("--master")
args = parser.parse_args()


master_claims = set()
with open(args.master,"r") as f:
    for line in f:
        claim = json.loads(line)["claim"]
        master_claims.add(claim.replace(".","").lower().strip())

with open(args.in_file,"r") as f:
    for line in f:
        claim = json.loads(line)
        if not claim["claim"].replace(".","").lower().strip() in master_claims:
            print(json.dumps(claim))