import json
import os
import re
import spacy
from argparse import ArgumentParser
from copy import deepcopy

from tqdm import tqdm

parser = ArgumentParser()
parser.add_argument("--in-file",type=str)
parser.add_argument("--out-dir",type=str)

args = parser.parse_args()


nlp = spacy.load('en_core_web_sm')



if not os.path.exists(args.out_dir):
    os.makedirs(args.out_dir)

class ReplacementRule:

    def process_instance(self, instance):
        return self._process(instance)

    def _process(self, instance):
        raise NotImplementedError("Not implemented here")

    def name(self):
        raise NotImplementedError("NotImplemented")


class IsAReplacementRuleMeaningAltering(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "{0} is not a {1}.".format(matches1.group(1).replace(".",""),matches1.group(2).replace(".",""))
        else:
            new_claim = "{0} is not an {1}.".format(matches2.group(1).replace(".", ""), matches2.group(2).replace(".",""))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "is.a.swap"

class WasAReplacementRuleMeaningAltering(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "{0} was not a {1}.".format(matches1.group(1).replace(".",""),matches1.group(2).replace(".",""))
        else:
            new_claim = "{0} was not an {1}.".format(matches2.group(1).replace(".", ""), matches2.group(2).replace(".",""))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "was.a.swap"


class IsAReplacementRuleMeaningAltering1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "{0} is not a {1}.".format(matches1.group(1).replace(".",""),matches1.group(2).replace(".",""))
        else:
            new_claim = "{0} is not an {1}.".format(matches2.group(1).replace(".", ""), matches2.group(2).replace(".",""))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "is.a.swap.2"

class WasAReplacementRuleMeaningAltering1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "{0} wasn't a {1}.".format(matches1.group(1).replace(".",""),matches1.group(2).replace(".",""))
        else:
            new_claim = "{0} wasn't an {1}.".format(matches2.group(1).replace(".", ""), matches2.group(2).replace(".",""))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "was.a.swap.2"

class IsAReplacementRuleMeaningAltering2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "{0} is definitely not a {1}.".format(matches1.group(1).replace(".",""),matches1.group(2).replace(".",""))
        else:
            new_claim = "{0} is definitely not an {1}.".format(matches2.group(1).replace(".", ""), matches2.group(2).replace(".",""))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "is.intens1.a.swap.2"

class WasAReplacementRuleMeaningAltering2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "{0} definitely was not a {1}.".format(matches1.group(1).replace(".",""),matches1.group(2).replace(".",""))
        else:
            new_claim = "{0} definitely was not an {1}.".format(matches2.group(1).replace(".", ""), matches2.group(2).replace(".",""))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "was.intens1.a.swap.2"

class IsAReplacementRuleMeaningAltering3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "{0} is certainly not a {1}.".format(matches1.group(1).replace(".",""),matches1.group(2).replace(".",""))
        else:
            new_claim = "{0} is certainly not an {1}.".format(matches2.group(1).replace(".", ""), matches2.group(2).replace(".",""))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "is.intens2.a.swap.2"

class WasAReplacementRuleMeaningAltering3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "{0} certainly was not a {1}.".format(matches1.group(1).replace(".",""),matches1.group(2).replace(".",""))
        else:
            new_claim = "{0} certainly was not an {1}.".format(matches2.group(1).replace(".", ""), matches2.group(2).replace(".",""))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "was.intens2.a.swap.2"

class DirectedByMeaningAltering(ReplacementRule):
    def _process(self, instance):

        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None:
            return None
        new_claim = "{0} is not directed by {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "directedby.swap.1"

class DirectedByMeaningAltering1(ReplacementRule):
    def _process(self, instance):

        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None:
            return None
        new_claim = "{0} isn't directed by {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "directedby.swap.2"


class DirectedByMeaningAltering2(ReplacementRule):
    def _process(self, instance):

        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None:
            return None
        new_claim = "{0} is definitely not directed by {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "directedby.intens1.swap.1"

class DirectedByMeaningAltering3(ReplacementRule):
    def _process(self, instance):

        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None:
            return None
        new_claim = "{0} is certainly not directed by {1}.".format(matches1.group(1).replace(".", ""),
                                                                    matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "directedby.intens2.swap.1"


class StarredIn1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:starred|stars) in (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        new_claim = "{0} did not star in {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "starredin1.swap"

class StarredIn2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:starred|stars) in (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        new_claim = "{0} didn't star in {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "starredin2.swap"


class American(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) American (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None

        instance["claim"] = instance["claim"].replace("American","Canadian")
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "american.canadian"


class Birth1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is) born (?:in|on)? (.+)", instance["claim"])

        if matches1 is None:
            return None
        if instance["label"] == "NOT ENOUGH INFO":
            return None


        instance["claim"] = instance["claim"].replace("born","not born")
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "birth1.swap"



class Birth2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is) born (?:in|on)? (.+)", instance["claim"])

        if matches1 is None:
            return None
        if instance["label"] == "NOT ENOUGH INFO":
            return None

        instance["claim"] = "{0} was never born".format(matches1.group(1).replace(".", ""))
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "birth2.swap"





class Death1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) died (?:in|on) (.+)", instance["claim"])

        if matches1 is None:
            return None
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        new_claim = "{0} is still alive".format(matches1.group(1).replace(".", ""))
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        instance["claim"] = new_claim

        return instance

    def name(self):
        return "death1.swap"

class Death2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) died (?:in|on) (.+)", instance["claim"])

        if matches1 is None:
            return None
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        new_claim = "{0} has not died".format(matches1.group(1).replace(".", ""))
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        instance["claim"] = new_claim

        return instance

    def name(self):
        return "death2.swap"





class ClaimRewriter:

    def __init__(self, out_dir):
        self.replacement_rules = [IsAReplacementRuleMeaningAltering(),
                                  WasAReplacementRuleMeaningAltering(),
                                  IsAReplacementRuleMeaningAltering1(),
                                  WasAReplacementRuleMeaningAltering1(),
                                  IsAReplacementRuleMeaningAltering2(),
                                  WasAReplacementRuleMeaningAltering2(),
                                  IsAReplacementRuleMeaningAltering3(),
                                  WasAReplacementRuleMeaningAltering3(),
                                  DirectedByMeaningAltering(),
                                  DirectedByMeaningAltering1(),
                                  DirectedByMeaningAltering2(),
                                  DirectedByMeaningAltering3(),
                                  StarredIn1(),
                                  StarredIn2(),
                                  American(),
                                  Birth1(),
                                  Birth2(),
                                  Death1(),
                                  Death2()
                                  ]

        self.changed_files = {rule:open(out_dir+"/changed."+rule.name()+".jsonl","w+") for rule in self.replacement_rules}
        self.unchanged_files = {rule:open(out_dir+"/unchanged."+rule.name()+".jsonl","w+") for rule in self.replacement_rules}


    def process_claim(self, claim):
        for rule in self.replacement_rules:
            rep_claim = rule.process_instance(deepcopy(claim))

            if rep_claim is not None:
                self.unchanged_files[rule].write(json.dumps(claim)+"\n")
                self.changed_files[rule].write(json.dumps(rep_claim)+"\n")



with open(args.in_file) as f:
    rewriter = ClaimRewriter(args.out_dir)
    for line in tqdm(f):
        line = json.loads(line)
        rewriter.process_claim(line)

    out_dir_name = args.out_dir.split("/")[-1]


with open("generated2.sh","w+") as f:
    for rule in rewriter.replacement_rules:
        f.write("bash scripts/run_oracle.sh {0} changed.{1}.jsonl".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("bash scripts/run_oracle.sh {0} unchanged.{1}.jsonl".format(out_dir_name, rule.name()))
        f.write("\n")

    for rule in rewriter.replacement_rules:
        f.write("bash scripts/run_full.sh {0} changed.{1}.jsonl".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("bash scripts/run_full.sh {0} unchanged.{1}.jsonl".format(out_dir_name, rule.name()))
        f.write("\n")

    for rule in rewriter.replacement_rules:
        f.write("echo {0} changed.oracle.{1} >> {0}.oracle_scores".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("bash scripts/run_scoring_oracle.sh {0} changed.{1}.jsonl >> {0}.oracle_scores".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("echo {0} unchanged.oracle.{1} >> {0}.oracle_scores".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("bash scripts/run_scoring_oracle.sh {0} unchanged.{1}.jsonl >> {0}.oracle_scores".format(out_dir_name, rule.name()))
        f.write("\n")

    for rule in rewriter.replacement_rules:
        f.write("echo {0} changed.full.{1} >> {0}.full_scores".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("bash scripts/run_scoring_full.sh {0} changed.{1}.jsonl >> {0}.full_scores".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("echo {0} unchanged.full.{1} >> {0}.full_scores".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("bash scripts/run_scoring_full.sh {0} unchanged.{1}.jsonl >> {0}.full_scores".format(out_dir_name, rule.name()))
        f.write("\n")




