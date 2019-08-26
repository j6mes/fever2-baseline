from collections import defaultdict

import numpy as np
import json
import argparse

np.random.seed(123)

parser = argparse.ArgumentParser()
parser.add_argument("--in-files",type=str)
parser.add_argument("--out-file",type=str)
parser.add_argument("--names",type=str)
args = parser.parse_args()

claims = []

skip = -1
for file in args.in_files.split(","):
    with open(file) as f:
        for id,line in enumerate(f):
            l = json.loads(line)
            l["name"] = file.split(".")[0]
            l["num"] = id
            if file.startswith("rules") and l["label"] == "NOT ENOUGH INFO":
                skip -=1
                if skip > 0:
                    continue
            claims.append(l)

np.random.shuffle(claims)

with open(args.out_file, "w+") as outfile:
    for id, line in enumerate(claims):
        line['id'] = id + 500000
        line["attack"] = line["attack"] if "attack" in line else line["rule"]

        file_idx = line["num"]+1
        try:
            with open("../TEST DATA FINAL/{}/claim-{}.txt".format(line["name"],str(file_idx).zfill(2)),"r") as f:
                lines = f.readlines()
                line["annotation"]=" ".join([l for l in lines if l.startswith("*")]).replace("\n","").replace("*","")
        except:
            line["annotation"] = "N/A"
        if "rule" in line:
            del line["rule"]
        if "verifiable" in line:
            del line["verifiable"]
#        del line["label"]
#        del line["evidence"]
#        del line["name"]
        del line["num"]
        outfile.write(json.dumps(line) + "\n")