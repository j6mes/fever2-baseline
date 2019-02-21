import json
from copy import deepcopy

from tqdm import tqdm

from rewrites.complex_negate import *
from rewrites.label_preserving import *
from rewrites.simple_negate import *

class ClaimRewriter:
    def __init__(self, transformation, rules):
        self.transformation = transformation
        self.replacement_rules = rules

    def process_claim(self, claim):
        ret_changed = []
        ret_unchanged = []
        for rule in self.replacement_rules:
            rep_claim = rule.process_instance(deepcopy(claim))

            if rep_claim is not None:
                rep_claim["original_id"] = claim["id"]
                rep_claim["transformation"] = self.transformation
                rep_claim["rule"] = rule.name()
                ret_changed.append(rep_claim)
                ret_unchanged.append(claim)

        return ret_changed, ret_unchanged

class ComplexNegateClaimRewriter(ClaimRewriter):
    def __init__(self):
        rules = [ComplexNegateIsAReplacementRule1(),
                          ComplexNegateIsAReplacementRule2(),
                          ComplexNegateIsAReplacementRule3(),
                          ComplexNegateIsAReplacementRule4(),
                          ComplexNegateIsAReplacementRule5(),
                          ComplexNegateWasAReplacementRule1(),
                          ComplexNegateWasAReplacementRule2(),
                          ComplexNegateWasAReplacementRule3(),
                          ComplexNegateWasAReplacementRule4(),
                          ComplexNegateWasAReplacementRule5(),
                          ComplexNegateDirectedBy1(),
                          ComplexNegateDirectedBy2(),
                          ComplexNegateDirectedBy3(),
                          ComplexNegateDirectedBy4(),
                          ComplexNegateDirectedBy5(),
                          ComplexNegateAmerican(),
                          ComplexNegateBirth1(),
                          ComplexNegateBirth2(),
                          ComplexNegateBirth3(),
                          ComplexNegateBirth4(),
                          ComplexNegateDeath1(),
                          ComplexNegateDeath2(),
                          ComplexNegateDeath3()
                          ]
        super().__init__("complex_negate",
                         rules)




class LabelPreservingClaimRewriter(ClaimRewriter):

    def __init__(self):
        rules  =[LabelPreservingIsAReplacementRule1(),
                          LabelPreservingIsAReplacementRule2(),
                          LabelPreservingIsAReplacementRule3(),
                          LabelPreservingIsAReplacementRule4(),
                          LabelPreservingIsAReplacementRule5(),
                          LabelPreservingIsAReplacementRule6(),
                          LabelPreservingWasAReplacementRule1(),
                          LabelPreservingWasAReplacementRule2(),
                          LabelPreservingWasAReplacementRule3(),
                          LabelPreservingWasAReplacementRule4(),
                          LabelPreservingWasAReplacementRule5(),
                          LabelPreservingWasAReplacementRule6(),
                          LabelPreservingDirectedBy1(),
                          LabelPreservingDirectedBy2(),
                          LabelPreservingDirectedBy3(),
                          LabelPreservingDirectedBy4(),
                          LabelPreservingDirectedBy5(),
                          LabelPreservingAmerican(),
                          LabelPreservingBirth1(),
                          LabelPreservingBirth2(),
                          LabelPreservingDeath1(),
                          LabelPreservingDeath2(),
                          LabelPreservingDeath3()
                          ]
        super().__init__("label_preserving",
                         rules)

class SimpleNegateClaimRewriter(ClaimRewriter):

    def __init__(self):
        rules = [SimpleNegateIsAReplacementRuleMeaningAltering(),
                          SimpleNegateWasAReplacementRuleMeaningAltering(),
                          SimpleNegateIsAReplacementRuleMeaningAltering1(),
                          SimpleNegateWasAReplacementRuleMeaningAltering1(),
                          SimpleNegateIsAReplacementRuleMeaningAltering2(),
                          SimpleNegateWasAReplacementRuleMeaningAltering2(),
                          SimpleNegateIsAReplacementRuleMeaningAltering3(),
                          SimpleNegateWasAReplacementRuleMeaningAltering3(),
                          SimpleNegateDirectedByMeaningAltering(),
                          SimpleNegateDirectedByMeaningAltering1(),
                          SimpleNegateDirectedByMeaningAltering2(),
                          SimpleNegateDirectedByMeaningAltering3(),
                          SimpleNegateStarredIn1(),
                          SimpleNegateStarredIn2(),
                          SimpleNegateAmerican(),
                          SimpleNegateBirth1(),
                          SimpleNegateBirth2(),
                          SimpleNegateDeath1(),
                          SimpleNegateDeath2()
                          ]
        super().__init__("simple_negate",
                         rules)



def process(in_file, changed_file, unchanged_file):
    all_unchanged = {}
    all_changed = []
    with open(in_file) as f:
        rewriters =  [LabelPreservingClaimRewriter(), SimpleNegateClaimRewriter(), ComplexNegateClaimRewriter()]

        for line in tqdm(f):
            line = json.loads(line)
            for rewriter in rewriters:
                changed, unchanged = rewriter.process_claim(line)
                all_unchanged.update({item["id"]:item for item in unchanged})
                all_changed.extend(changed)

    maxidx = 0
    with open(unchanged_file,"w+") as f:
        for item in all_unchanged.values():
            maxidx = max(maxidx, item["id"])
            f.write(json.dumps(item)+"\n")

    with open(changed_file, "w+") as f:
        for idx, item in enumerate(all_changed):
            item["id"] = idx + maxidx + int(1e7)
            f.write(json.dumps(item)+"\n")


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("--in-file", type=str)
    parser.add_argument("--changed-file", type=str)
    parser.add_argument("--unchanged-file", type=str)

    args = parser.parse_args()

    process(args.in_file, args.changed_file, args.unchanged_file)

