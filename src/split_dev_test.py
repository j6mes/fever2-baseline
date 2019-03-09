import json

from tqdm import tqdm

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("--dev-file", type=str)
    parser.add_argument("--test-file", type=str)
    parser.add_argument("--all-in-changed", type=str)
    parser.add_argument("--all-in-unchanged", type=str)
    parser.add_argument("--dev-out-changed", type=str)
    parser.add_argument("--test-out-changed", type=str)
    parser.add_argument("--dev-out-unchanged", type=str)
    parser.add_argument("--test-out-unchanged", type=str)

    args = parser.parse_args()

    dev_ids = set()
    test_ids = set()

    with open(args.dev_file,"r") as dev_file:
        for line in dev_file:
            claim = json.loads(line)
            dev_ids.add(claim["id"])

    with open(args.test_file, "r") as test_file:
        for line in test_file:
            claim = json.loads(line)
            test_ids.add(claim["id"])

    print(len(dev_ids),len(test_ids))
    changed_dev = []
    changed_test = []
    with open(args.all_in_changed, "r") as in_file:
        for line in in_file:
            claim = json.loads(line)
            if claim["original_id"] in dev_ids:
                changed_dev.append(claim)
            elif claim["original_id"] in test_ids:
                changed_test.append(claim)

    unchanged_dev = []
    unchanged_test = []
    with open(args.all_in_unchanged, "r") as in_file:
        for line in in_file:
            claim = json.loads(line)
            if claim["id"] in dev_ids:
                unchanged_dev.append(claim)
            elif claim["id"] in test_ids:
                unchanged_test.append(claim)

    with open(args.dev_out_changed, "w+") as diff_file:
        for idx,claim in enumerate(changed_dev):
            claim["id"] = 2e7+idx
            diff_file.write(json.dumps(claim)+"\n")

    with open(args.test_out_changed, "w+") as diff_file:
        for idx,claim in enumerate(changed_test):
            claim["id"] = 3e7+idx
            diff_file.write(json.dumps(claim)+"\n")

    with open(args.dev_out_unchanged, "w+") as diff_file:
        for idx,claim in enumerate(unchanged_dev):
            diff_file.write(json.dumps(claim)+"\n")

    with open(args.test_out_unchanged, "w+") as diff_file:
        for idx,claim in enumerate(unchanged_test):
            diff_file.write(json.dumps(claim)+"\n")
