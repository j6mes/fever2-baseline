import json

from tqdm import tqdm

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("--old-file", type=str)
    parser.add_argument("--new-file", type=str)
    parser.add_argument("--diff-new", type=str)
    parser.add_argument("--diff-minus", type=str)

    args = parser.parse_args()


    old_claims = dict()
    new_claims = dict()

    with open(args.old_file,"r") as old_file:
        for idx,line in enumerate(old_file):
            claim = json.loads(line)

            old_claims[claim["claim"]] = (claim, idx)

    with open(args.new_file, "r") as new_file:
        for idx,line in enumerate(new_file):
            claim = json.loads(line)

            new_claims[claim["claim"]] = (claim,idx)

    print(len(new_claims.keys()))
    print(len(old_claims.keys()))
    print(len(set(new_claims.keys()).intersection(old_claims.keys())))
    diff = set(new_claims.keys()).difference(set(old_claims.keys()))
    diff_minus = set(new_claims.keys()).intersection(old_claims.keys())

    with open(args.diff_new, "w+") as diff_file:
        for claim in diff:
            claim = new_claims[claim][0]
            diff_file.write(json.dumps(claim)+"\n")

    with open(args.diff_minus, "w+") as diff_minus_file:
        for claim in tqdm(diff_minus):
            claim = old_claims[claim][0]
            diff_minus_file.write(json.dumps(claim)+"\n")
