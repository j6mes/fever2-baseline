import re
import spacy
from rewrites.replacement_rule import ReplacementRule

nlp = spacy.load('en_core_web_sm')

class ComplexNegateIsAReplacementRule1(ReplacementRule):
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



class ComplexNegateIsAReplacementRule2(ReplacementRule):
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



class ComplexNegateIsAReplacementRule3(ReplacementRule):
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



class ComplexNegateIsAReplacementRule4(ReplacementRule):
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



class ComplexNegateIsAReplacementRule5(ReplacementRule):
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


class ComplexNegateWasAReplacementRule1(ReplacementRule):
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


class ComplexNegateWasAReplacementRule2(ReplacementRule):
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


class ComplexNegateWasAReplacementRule3(ReplacementRule):
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


class ComplexNegateWasAReplacementRule4(ReplacementRule):
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


class ComplexNegateWasAReplacementRule5(ReplacementRule):
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


class ComplexNegateDirectedBy1(ReplacementRule):
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

class ComplexNegateDirectedBy2(ReplacementRule):
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


class ComplexNegateDirectedBy3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        new_claim = "There is a movie called {0}, {1} has no involvement in its production.".format(
            matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim
        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        return instance

    def name(self):
        return "directedby3"


class ComplexNegateDirectedBy4(ReplacementRule):
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


class ComplexNegateDirectedBy5(ReplacementRule):
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


class ComplexNegateStarredIn1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:starred|stars) in (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        new_claim = "There is a person, {0}, that did not star in {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))

        instance["label"] = "REFUTES" if instance["label"] == "SUPPORTS" else "SUPPORTS"
        instance["claim"] = new_claim
        return instance

    def name(self):
        return "starredin1"

class ComplexNegateStarredIn2(ReplacementRule):
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


class ComplexNegateStarredIn3(ReplacementRule):
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

class ComplexNegateStarredIn4(ReplacementRule):
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



class ComplexNegateAmerican(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) an American (.+)", instance["claim"])
        if instance["label"] == "NOT ENOUGH INFO":
            return None
        if matches1 is None:
            return None
        if instance["label"] == "REFUTES":
            return None

        new_claim = "{0} {1} that originated from outside the United States.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))

        instance["claim"] = new_claim
        instance["label"] = "REFUTES"

        return instance

    def name(self):
        return "american"


class ComplexNegateBirth1(ReplacementRule):
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


class ComplexNegateBirth2(ReplacementRule):
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

class ComplexNegateBirth3(ReplacementRule):
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


class ComplexNegateBirth4(ReplacementRule):
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


class ComplexNegateDeath1(ReplacementRule):
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


class ComplexNegateDeath2(ReplacementRule):
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


class ComplexNegateDeath3(ReplacementRule):
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

