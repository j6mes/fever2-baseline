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


class IsAReplacementRule1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There exists a {0} called {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There exists an {0} called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "there.exists.a.called"


class IsAReplacementRule3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There exists a {0} that goes by the name of {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There exists an {0} that goes by the name of {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "there.exists.a.that.goes.by.name.of"



class IsAReplacementRule2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There is a {0} called {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1))
        else:
            new_claim = "There is an {0} called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim
        return instance

    def name(self):
        return "there.is.a.called"



class IsAReplacementRule4(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There exists a {0} called {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There exists an {0} called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "there.exists.a.called.prn"


class IsAReplacementRule5(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There exists a {0}, it goes by the name of {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There exists an {0}, it goes by the name of {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "there.exists.a.that.goes.by.name.of.prn"



class IsAReplacementRule6(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There is a {0}, it is called {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1))
        else:
            new_claim = "There is an {0}, it is called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim
        return instance

    def name(self):
        return "there.is.a.called.prn"


class WasAReplacementRule1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There existed a {0} called {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There existed an {0} called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "there.existed.a.called"


class WasAReplacementRule3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There existed a {0} that went by the name of {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There existed an {0} that went by the name of {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "there.existed.a.that.went.by.name.of"



class WasAReplacementRule2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There was a {0} called {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1))
        else:
            new_claim = "There was an {0} called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim
        return instance

    def name(self):
        return "there.was.a.called"


class WasAReplacementRule4(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There existed a {0}, it was called {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There existed an {0}, it was called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "there.existed.a.called.prn"


class WasAReplacementRule5(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There existed a {0}, it went by the name of {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There existed an {0}, it went by the name of {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "there.existed.a.that.went.by.name.of.prn"



class WasAReplacementRule6(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There was a {0}, it was called {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1))
        else:
            new_claim = "There was an {0}, it was called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim
        return instance

    def name(self):
        return "there.was.a.called.prn"



class DirectedBy1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if matches1 is None:
            return None
        new_claim = "There is a movie called {0} which is directed by {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim

        return instance

    def name(self):
        return "directedby1"

class DirectedBy4(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if matches1 is None:
            return None
        new_claim = "{1} is the director of {0}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim

        return instance

    def name(self):
        return "directedby4"

class DirectedBy5(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if matches1 is None:
            return None
        new_claim = "{1} was the director of {0}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim

        return instance

    def name(self):
        return "directedby5"

class DirectedBy2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if matches1 is None:
            return None

        new_claim = "There is a director, {0}, who was involved in the production of {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1).replace(".", ""))
        instance["claim"] = new_claim
        return instance

    def name(self):
        return "directedby2"


class DirectedBy3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if matches1 is None:
            return None
        new_claim = "There is a person involved in the movie industry, {0}, who was the director of {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1).replace(".", ""))
        instance["claim"] = new_claim
        return instance

    def name(self):
        return "directedby3"


class StarredIn1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:starred|stars) in (.+)", instance["claim"])

        if matches1 is None:
            return None
        new_claim = "There is a person, {0}, that starred in {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))

        instance["claim"] = new_claim
        return instance

    def name(self):
        return "starredin1"

class StarredIn2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:starred|stars) in (.+)", instance["claim"])

        if matches1 is None:
            return None
        new_claim = "There is a person, {0}, that took a leading acting role in {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim
        return instance

    def name(self):
        return "starredin2"


class American(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) an American (.+)", instance["claim"])

        if matches1 is None:
            return None
        new_claim = "{0} {1} that originated from the United States.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "american"


class Birth1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is) born (?:in|on)? (.+)", instance["claim"])

        if matches1 is None:
            return None

        doc = nlp(instance["claim"])

        is_place = any([e.label_ in ["GPE","LOC"] for e in doc.ents])
        is_time = any([e.label_ in ["TIME","DATE","ORDINAL", "CARDINAL"] for e in doc.ents])

        if is_place and not is_time:
            new_claim = "There exists a place, {1}, that is the birthplace of the person {0}.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))
        elif is_time and not is_place:
            new_claim = "{1} is the approximate time at which the person {0} was born.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))

        else:
            return None

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "birth1"


class Birth2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is) born (?:in|on)? (.+)", instance["claim"])

        if matches1 is None:
            return None

        doc = nlp(instance["claim"])

        is_place = any([e.label_ in ["GPE","LOC"] for e in doc.ents])
        is_time = any([e.label_ in ["TIME","DATE","ORDINAL", "CARDINAL"] for e in doc.ents])

        if is_place and not is_time:
            new_claim = "There exists a place, {1}, that is where the person {0} started living.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))
        elif is_time and not is_place:
            new_claim = "{1} is the approximate time at which the person {0} started living.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))

        else:
            return None

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "birth2"


class Death1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) died (?:in|on) (.+)", instance["claim"])

        if matches1 is None:
            return None

        doc = nlp(instance["claim"])

        is_place = any([e.label_ in ["GPE","LOC"] for e in doc.ents])
        is_time = any([e.label_ in ["TIME","DATE","ORDINAL", "CARDINAL"] for e in doc.ents])

        if is_place and not is_time:
            new_claim = "There exists a place, {1}, that is the place where the person {0} became deceased.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))
        elif is_time and not is_place:
            new_claim = "{1} is the approximate time at which the person {0} became deceased.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))

        else:
            return None

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "death1"


class Death2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) died (?:in|on) (.+)", instance["claim"])

        if matches1 is None:
            return None

        doc = nlp(instance["claim"])

        is_place = any([e.label_ in ["GPE","LOC"] for e in doc.ents])
        is_time = any([e.label_ in ["TIME","DATE","ORDINAL", "CARDINAL"] for e in doc.ents])

        if is_place and not is_time:
            new_claim = "There exists a place, {1}, that is the place where the person {0} died.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))
        elif is_time and not is_place:
            new_claim = "{1} is the approximate time at which the person {0} died.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))

        else:
            return None

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "death2"


class Death3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) died (?:in|on) (.+)", instance["claim"])

        if matches1 is None:
            return None

        doc = nlp(instance["claim"])

        is_place = any([e.label_ in ["GPE","LOC"] for e in doc.ents])
        is_time = any([e.label_ in ["TIME","DATE","ORDINAL", "CARDINAL"] for e in doc.ents])

        if is_place and not is_time:
            new_claim = "There exists a place, {1}, that is the place where the person {0} took their final breath.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))
        elif is_time and not is_place:
            new_claim = "{1} is the approximate time at which the person {0} took their final breath.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))

        else:
            return None

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "death3"



class ClaimRewriter:

    def __init__(self, out_dir):
        self.replacement_rules = [IsAReplacementRule1(),
                                  IsAReplacementRule2(),
                                  IsAReplacementRule3(),
                                  IsAReplacementRule4(),
                                  IsAReplacementRule5(),
                                  IsAReplacementRule6(),
                                  WasAReplacementRule1(),
                                  WasAReplacementRule2(),
                                  WasAReplacementRule3(),
                                  WasAReplacementRule4(),
                                  WasAReplacementRule5(),
                                  WasAReplacementRule6(),
                                  DirectedBy1(),
                                  DirectedBy2(),
                                  DirectedBy3(),
                                  DirectedBy4(),
                                  DirectedBy5(),
                                  American(),
                                  Birth1(),
                                  Birth2(),
                                  Death1(),
                                  Death2(),
                                  Death3()
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


with open("generated1.sh","w+") as f:
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
        f.write("echo {0} changed.oracle.{1} >> oracle_scores".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("bash scripts/run_scoring_oracle.sh {0} changed.{1}.jsonl >> oracle_scores".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("echo {0} unchanged.oracle.{1} >> oracle_scores".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("bash scripts/run_scoring_oracle.sh {0} unchanged.{1}.jsonl >> oracle_scores".format(out_dir_name, rule.name()))
        f.write("\n")

    for rule in rewriter.replacement_rules:
        f.write("echo {0} changed.full.{1} >> full_scores".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("bash scripts/run_scoring_full.sh {0} changed.{1}.jsonl >> full_scores".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("echo {0} unchanged.full.{1} >> full_scores".format(out_dir_name, rule.name()))
        f.write("\n")
        f.write("bash scripts/run_scoring_full.sh {0} unchanged.{1}.jsonl >> full_scores".format(out_dir_name, rule.name()))
        f.write("\n")




