from collections import defaultdict

import numpy as np
import json
import argparse

np.random.seed(123)

parser = argparse.ArgumentParser()
parser.add_argument("--in-files",type=str)
parser.add_argument("--out-file",type=str)

args = parser.parse_args()

claims = []

for file in args.in_files.split(","):
    with open(file) as f:
        for line in f:
            claims.append(json.loads(line))

np.random.shuffle(claims)

with open(args.out_file, "w+") as outfile:
    for id, line in enumerate(claims):
        line['id'] = id + 500000
        line["attack"] = "redacted"
        outfile.write(json.dumps(line) + "\n")
