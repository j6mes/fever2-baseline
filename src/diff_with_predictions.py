import collections
import json
from collections import OrderedDict as dict
from tqdm import tqdm

class OrderedSet(collections.MutableSet):

    def __init__(self, iterable=None):
        self.end = end = []
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("--old-file", type=str)
    parser.add_argument("--new-file", type=str)
    parser.add_argument("--diff-new", type=str)
    parser.add_argument("--diff-minus", type=str)
    parser.add_argument("--old-file-predictions",type=str)
    parser.add_argument("--diff-minus-predictions",type=str)
    args = parser.parse_args()


    old_claims = dict()
    new_claims = dict()

    old_predictions = []

    with open(args.old_file,"r") as old_file:
        for idx,line in enumerate(old_file):
            claim = json.loads(line)

            old_claims[claim["claim"]] = (claim, idx)

    with open(args.new_file, "r") as new_file:
        for idx,line in enumerate(new_file):
            claim = json.loads(line)

            new_claims[claim["claim"]] = (claim,idx)

    with open(args.old_file_predictions, "r") as old_predictions_file:
        old_predictions = old_predictions_file.readlines()

    diff = OrderedSet(new_claims.keys()) - old_claims.keys()
    diff_minus = OrderedSet(new_claims.keys()) & old_claims.keys()

    with open(args.diff_new, "w+") as diff_file:
        for claim in diff:
            claim = new_claims[claim][0]
            diff_file.write(json.dumps(claim)+"\n")

    with open(args.diff_minus, "w+") as diff_minus_file:
        for claim in tqdm(diff_minus):
            claim = old_claims[claim][0]
            diff_minus_file.write(json.dumps(claim)+"\n")

    with open(args.diff_minus_predictions, "w+") as diff_minus_predictions:
        for claim in tqdm(diff_minus):
            idx = old_claims[claim][1]
            print(idx)
            diff_minus_predictions.write(old_predictions[idx])
