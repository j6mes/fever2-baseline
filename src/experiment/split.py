import argparse
import json
import os
from collections import defaultdict

parser = argparse.ArgumentParser()

parser.add_argument("--changed-file")
parser.add_argument("--changed-file-predictions")
parser.add_argument("--original-file")
parser.add_argument("--original-file-predictions")
parser.add_argument("--destination")

args = parser.parse_args()

original_claims = dict()
predictions = dict()
unchanged_predictions = dict()
changed_claims = defaultdict(list)

with open(args.original_file,"r") as file:
    for line in file:
        line = json.loads(line)
        original_claims[line["id"]] = line

with open(args.changed_file,"r") as file:
    for line in file:
        line = json.loads(line)
        changed_claims[line["transformation"]] = line

with open(args.changed_file_predictions,"r") as file:
    for line in file:
        line = json.loads(line)
        predictions[line["id"]] = line

with open(args.original_file_predictions,"r") as file:
    for line in file:
        line = json.loads(line)
        unchanged_predictions[line["id"]] = line


os.makedirs(args.destination,exist_ok=True)
for transformation in changed_claims.keys():
    with open(args.destination+"/"+transformation+".predictions.jsonl","w+") as predictions_file, \
            open(args.destination + "/" + transformation + ".changed.jsonl", "w+") as changed_file, \
            open(args.destination + "/" + transformation+".original.predictions.jsonl", "w+") as unchanged_predictions_file, \
            open(args.destination + "/" + transformation+".original.jsonl", "w+") as original_file:

        for item in changed_claims[transformation]:
            changed_file.write(json.dumps(item)+"\n")
            predictions_file.write(json.dumps(predictions[item["id"]])+"\n")
            unchanged_predictions_file.write(json.dumps(unchanged_predictions[item["id"]])+"\n")
            original_file.write(json.dumps(original_claims[item["id"]])+"\n")

