import argparse
import json
import random
parser = argparse.ArgumentParser()
parser.add_argument("--in-file")
args = parser.parse_args()

instances = []

for claim in open(args.in_file):
    sample = json.loads(claim, encoding='utf8')
    sample["claim"] = sample["question"]
    sample["label"] = "SUPPORTS" if sample["answer"] else "REFUTES"
    sample["evidence"] = []
    instances.append(sample)


random.seed(123)
random.shuffle(instances)

for sample in instances[:100]:
    print(json.dumps(sample))


