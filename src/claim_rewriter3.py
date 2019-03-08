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

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There does not exist a {0} called {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There does not exist an {0} called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "there.does.not.exist.a.called"



class IsAReplacementRule2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is (?:a|an) (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None:
            return None


        new_claim = "There exists no {0} called {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "there.exists.no.a.called"



class IsAReplacementRule3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There does not exist a {0} that goes by the name of {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There does not exist an {0} that goes by the name of {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "there.not.exist.named"



class IsAReplacementRule4(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There is not a {0} called {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There is not an {0} called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "there.is.not.called"



class IsAReplacementRule5(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There is not a {0} that goes by the name of {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There is not an {0} that goes by the name of {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "there.is.not.by.name"


class WasAReplacementRule1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There did not exist a {0} called {1}.".format(matches1.group(2).replace(".", ""),
                                                                        matches1.group(1))
        else:
            new_claim = "There did not exist an {0} called {1}.".format(matches2.group(2).replace(".", ""),
                                                                         matches2.group(1))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "was.there.does.not.exist.a.called"


class WasAReplacementRule2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was (?:a|an) (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None:
            return None

        new_claim = "There existed no {0} called {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "was.there.exists.no.a.called"


class WasAReplacementRule3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There did not exist a {0} that goes by the name of {1}.".format(
                matches1.group(2).replace(".", ""), matches1.group(1))
        else:
            new_claim = "There did not exist an {0} that goes by the name of {1}.".format(
                matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "was.there.not.exist.named"


class WasAReplacementRule4(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There was not a {0} called {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1))
        else:
            new_claim = "There was not an {0} called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "was.there.is.not.called"


class WasAReplacementRule5(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None

        if matches1 is None and matches2 is None:
            return None

        if matches1 is not None:
            new_claim = "There was not a {0} that went by the name of {1}.".format(matches1.group(2).replace(".", ""),
                                                                                  matches1.group(1))
        else:
            new_claim = "There was not an {0} that went by the name of {1}.".format(matches2.group(2).replace(".", ""),
                                                                                   matches2.group(1))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "was.there.is.not.by.name"


class DirectedBy1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        new_claim = "There is a movie called {0} which is not directed by {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim

        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "directedby1"

class DirectedBy2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        new_claim = "There is a movie called {0} which wasn't directed by {1}.".format(
            matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim

        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "directedby2"


class DirectedBy3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        new_claim = "There is a movie called {0}, {1} has no involvement in the production.".format(
            matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "directedby3"


class DirectedBy4(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None

        new_claim = "There is a director, {0}, who was not involved in the production of {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1).replace(".", ""))
        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "directedby4"


class DirectedBy5(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        new_claim = "There is a person involved in the movie industry, {0}, who was not the director of {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1).replace(".", ""))
        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "directedby5"


class StarredIn1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:starred|stars) in (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        new_claim = "There is a person, {0}, that starred in {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))

        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        instance["claim"] = new_claim
        return instance

    def name(self):
        return "starredin1"

class StarredIn2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:starred|stars) in (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        new_claim = "There is a person, {0}, that did not take a leading acting role in {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "starredin2"


class StarredIn3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:starred|stars) in (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        new_claim = "There is a person, {0}, that did not appear in {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "starredin3"

class StarredIn4(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:starred|stars) in (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        new_claim = "There is a person, {0}, that had no role in {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "starredin4"



class American(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) an American (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None

        new_claim = "{0} {1} that originated from outside the United States.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "american"


class Birth1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is) born (?:in|on)? (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None

        doc = nlp(instance["claim"])

        is_place = any([e.label_ in ["GPE","LOC"] for e in doc.ents])
        is_time = any([e.label_ in ["TIME","DATE","ORDINAL", "CARDINAL"] for e in doc.ents])

        if is_place and not is_time:
            new_claim = "There exists a place, {1}, that was not the birthplace of the person {0}.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))
        elif is_time and not is_place:
            new_claim = "{1} is not the approximate time at which the person {0} was born.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))

        else:
            return None

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "birth1"


class Birth2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is) born (?:in|on)? (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None

        doc = nlp(instance["claim"])

        is_place = any([e.label_ in ["GPE","LOC"] for e in doc.ents])
        is_time = any([e.label_ in ["TIME","DATE","ORDINAL", "CARDINAL"] for e in doc.ents])

        if is_place and not is_time:
            new_claim = "There exists a place, {1}, that is not where the person {0} started living.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))
        elif is_time and not is_place:
            new_claim = "{1} is not the approximate time at which the person {0} started living.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))

        else:
            return None

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "birth2"

class Birth3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is) born (?:in|on)? (.+)", instance["claim"])

        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None

        doc = nlp(instance["claim"])

        is_place = any([e.label_ in ["GPE","LOC"] for e in doc.ents])
        is_time = any([e.label_ in ["TIME","DATE","ORDINAL", "CARDINAL"] for e in doc.ents])

        if is_place and not is_time:
            new_claim = "{0} was born in some other place than {1}.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))
        elif is_time and not is_place:
            new_claim = "{0} was born at some other time than {1}.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))

        else:
            return None

        instance["claim"] = new_claim

        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "birth3"


class Birth4(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is) born (?:in|on)? (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None

        doc = nlp(instance["claim"])

        is_place = any([e.label_ in ["GPE","LOC"] for e in doc.ents])
        is_time = any([e.label_ in ["TIME","DATE","ORDINAL", "CARDINAL"] for e in doc.ents])

        if is_place and not is_time:
            new_claim = "{1} is some place other than where the person {0} was born.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))
        elif is_time and not is_place:
            new_claim = "{1} is some other time than when {0} was born.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))

        else:
            return None

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "birth4"


class Death1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) died (?:in|on) (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None

        doc = nlp(instance["claim"])

        is_place = any([e.label_ in ["GPE","LOC"] for e in doc.ents])
        is_time = any([e.label_ in ["TIME","DATE","ORDINAL", "CARDINAL"] for e in doc.ents])

        if is_place and not is_time:
            new_claim = "{1} is somewhere other than the place where the person {0} became deceased.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))
        elif is_time and not is_place:
            new_claim = "{1} is some other time than when the person {0} became deceased.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))

        else:
            return None

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "death1"


class Death2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) died (?:in|on) (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None

        doc = nlp(instance["claim"])

        is_place = any([e.label_ in ["GPE","LOC"] for e in doc.ents])
        is_time = any([e.label_ in ["TIME","DATE","ORDINAL", "CARDINAL"] for e in doc.ents])

        if is_place and not is_time:
            new_claim = "There exists a place, {1}, that is not the place where the person {0} died.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))
        elif is_time and not is_place:
            new_claim = "{1} is not the when the person {0} died.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))

        else:
            return None

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

        return instance

    def name(self):
        return "death2"


class Death3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) died (?:in|on) (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None

        doc = nlp(instance["claim"])

        is_place = any([e.label_ in ["GPE","LOC"] for e in doc.ents])
        is_time = any([e.label_ in ["TIME","DATE","ORDINAL", "CARDINAL"] for e in doc.ents])

        if is_place and not is_time:
            new_claim = "There exists a place, {1}, that is not the place where the person {0} took their final breath.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))
        elif is_time and not is_place:
            new_claim = "{1} is not the approximate time at which the person {0} took their final breath.".format(matches1.group(1).replace(".", ""),
                                                                                matches1.group(2).replace(".", ""))

        else:
            return None

        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"

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
                                  WasAReplacementRule1(),
                                  WasAReplacementRule2(),
                                  WasAReplacementRule3(),
                                  WasAReplacementRule4(),
                                  WasAReplacementRule5(),
                                  DirectedBy1(),
                                  DirectedBy2(),
                                  DirectedBy3(),
                                  DirectedBy4(),
                                  DirectedBy5(),
                                  American(),
                                  Birth1(),
                                  Birth2(),
                                  Birth3(),
                                  Birth4(),
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


with open("generated3.sh","w+") as f:
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




