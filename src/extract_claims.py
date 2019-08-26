import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument("--in-file")
args = parser.parse_args()
for claim in open(args.in_file):
    print(json.loads(claim, encoding='utf8')["claim"])
