import re
from rewrites.replacement_rule import ReplacementRule


class SimpleNegateIsAReplacementRuleMeaningAltering(ReplacementRule):
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

class SimpleNegateWasAReplacementRuleMeaningAltering(ReplacementRule):
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


class SimpleNegateIsAReplacementRuleMeaningAltering1(ReplacementRule):
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

class SimpleNegateWasAReplacementRuleMeaningAltering1(ReplacementRule):
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

class SimpleNegateIsAReplacementRuleMeaningAltering2(ReplacementRule):
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

class SimpleNegateWasAReplacementRuleMeaningAltering2(ReplacementRule):
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

class SimpleNegateIsAReplacementRuleMeaningAltering3(ReplacementRule):
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

class SimpleNegateWasAReplacementRuleMeaningAltering3(ReplacementRule):
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

class SimpleNegateDirectedByMeaningAltering(ReplacementRule):
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

class SimpleNegateDirectedByMeaningAltering1(ReplacementRule):
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


class SimpleNegateDirectedByMeaningAltering2(ReplacementRule):
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

class SimpleNegateDirectedByMeaningAltering3(ReplacementRule):
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


class SimpleNegateStarredIn1(ReplacementRule):
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

class SimpleNegateStarredIn2(ReplacementRule):
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


class SimpleNegateAmerican(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) American (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        if instance["label"] == "REFUTES":
            return None

        instance["claim"] = instance["claim"].replace("American","Canadian")
        instance["label"] = "REFUTES"
        return instance

    def name(self):
        return "american.canadian"


class SimpleNegateBirth1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is) born (?:in|on)? (.+)", instance["claim"])

        if matches1 is None:
            return None
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if instance["label"] == "REFUTES":
            return None

        instance["claim"] = instance["claim"].replace("born","not born")
        instance["label"] = "REFUTES"
        return instance

    def name(self):
        return "birth1.swap"



class SimpleNegateBirth2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is) born (?:in|on)? (.+)", instance["claim"])

        if matches1 is None:
            return None
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if instance["label"] == "REFUTES":
            return None
        instance["claim"] = "{0} was never born".format(matches1.group(1).replace(".", ""))
        instance["label"] = "REFUTES"
        return instance

    def name(self):
        return "birth2.swap"





class SimpleNegateDeath1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) died (?:in|on) (.+)", instance["claim"])

        if matches1 is None:
            return None
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if instance["label"] == "REFUTES":
            return None

        new_claim = "{0} is still alive".format(matches1.group(1).replace(".", ""))
        instance["label"] = "REFUTES"
        instance["claim"] = new_claim

        return instance

    def name(self):
        return "death1.swap"

class SimpleNegateDeath2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) died (?:in|on) (.+)", instance["claim"])

        if matches1 is None:
            return None
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if instance["label"] == "REFUTES":
            return None
        new_claim = "{0} has not died".format(matches1.group(1).replace(".", ""))
        instance["label"] = "REFUTES"
        instance["claim"] = new_claim

        return instance

    def name(self):
        return "death2.swap"






