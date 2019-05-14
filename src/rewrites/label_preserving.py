import re
import spacy
from rewrites.replacement_rule import ReplacementRule

nlp = spacy.load('en_core_web_sm')

class LabelPreservingIsAReplacementRule1(ReplacementRule):
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


class LabelPreservingIsAReplacementRule3(ReplacementRule):
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



class LabelPreservingIsAReplacementRule2(ReplacementRule):
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



class LabelPreservingIsAReplacementRule4(ReplacementRule):
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


class LabelPreservingIsAReplacementRule5(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        doc = nlp(instance["claim"])
        is_person = any([e.label_ in ["PER"] for e in doc.ents])

        if is_person:
            return None

        if matches1 is not None:
            new_claim = "There exists a {0}, it goes by the name of {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There exists an {0}, it goes by the name of {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "there.exists.a.that.goes.by.name.of.prn"



class LabelPreservingIsAReplacementRule6(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) is a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) is an (.+)", instance["claim"])
        if matches1 is None and matches2 is None:
            return None

        doc = nlp(instance["claim"])
        is_person = any([e.label_ in ["PERSON"] for e in doc.ents])

        if matches1 is not None:
            if is_person:
                new_claim = "There is a {0}, they are called {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1))
            else:
                new_claim = "There is a {0}, it is called {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1))
        else:
            if is_person:
                new_claim = "There is an {0}, they are called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))
            else:
                new_claim = "There is an {0}, it is called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim
        return instance

    def name(self):
        return "there.is.a.called.prn"


class LabelPreservingWasAReplacementRule1(ReplacementRule):
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


class LabelPreservingWasAReplacementRule3(ReplacementRule):
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



class LabelPreservingWasAReplacementRule2(ReplacementRule):
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


class LabelPreservingWasAReplacementRule4(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])

        if matches1 is None and matches2 is None:
            return None

        doc = nlp(instance["claim"])
        is_person = any([e.label_ in ["PER"] for e in doc.ents])

        if is_person:
            return None

        if matches1 is not None:
            new_claim = "There existed a {0}, it was called {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There existed an {0}, it was called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "there.existed.a.called.prn"


class LabelPreservingWasAReplacementRule5(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])

        if matches1 is None and matches2 is None:
            return None

        doc = nlp(instance["claim"])
        is_person = any([e.label_ in ["PER"] for e in doc.ents])

        if is_person:
            return None

        if matches1 is not None:
            new_claim = "There existed a {0}, it went by the name of {1}.".format(matches1.group(2).replace(".",""),matches1.group(1))
        else:
            new_claim = "There existed an {0}, it went by the name of {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "there.existed.a.that.went.by.name.of.prn"



class LabelPreservingWasAReplacementRule6(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) was a (.+)", instance["claim"])
        matches2 = re.match(r"(.+) was an (.+)", instance["claim"])

        if matches1 is None and matches2 is None:
            return None

        doc = nlp(instance["claim"])
        is_person = any([e.label_ in ["PER"] for e in doc.ents])

        if is_person:
            return None

        if matches1 is not None:
            new_claim = "There was a {0}, it was called {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1))
        else:
            new_claim = "There was an {0}, it was called {1}.".format(matches2.group(2).replace(".", ""), matches2.group(1))

        instance["claim"] = new_claim
        return instance

    def name(self):
        return "there.was.a.called.prn"



class LabelPreservingDirectedBy1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if matches1 is None:
            return None
        new_claim = "There is a movie called {0} which is directed by {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim

        return instance

    def name(self):
        return "directedby1"

class LabelPreservingDirectedBy4(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if matches1 is None:
            return None
        new_claim = "{1} is the director of {0}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim

        return instance

    def name(self):
        return "directedby4"

class LabelPreservingDirectedBy5(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if matches1 is None:
            return None
        new_claim = "{1} was the director of {0}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim

        return instance

    def name(self):
        return "directedby5"

class LabelPreservingDirectedBy2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if matches1 is None:
            return None

        new_claim = "There is a director, {0}, who was involved in the production of {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1).replace(".", ""))
        instance["claim"] = new_claim
        return instance

    def name(self):
        return "directedby2"


class LabelPreservingDirectedBy3(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:was|is)? directed by (.+)", instance["claim"])
        if matches1 is None:
            return None
        new_claim = "There is a person involved in the movie industry, {0}, who was the director of {1}.".format(matches1.group(2).replace(".", ""), matches1.group(1).replace(".", ""))
        instance["claim"] = new_claim
        return instance

    def name(self):
        return "directedby3"


class LabelPreservingStarredIn1(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:starred|stars) in (.+)", instance["claim"])

        if matches1 is None:
            return None
        new_claim = "There is a person, {0}, that starred in {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))

        instance["claim"] = new_claim
        return instance

    def name(self):
        return "starredin1"

class LabelPreservingStarredIn2(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) (?:starred|stars) in (.+)", instance["claim"])

        if matches1 is None:
            return None
        new_claim = "There is a person, {0}, that took a leading acting role in {1}.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))
        instance["claim"] = new_claim
        return instance

    def name(self):
        return "starredin2"


class LabelPreservingAmerican(ReplacementRule):
    def _process(self, instance):
        matches1 = re.match(r"(.+) an American (.+)", instance["claim"])

        if matches1 is None:
            return None
        new_claim = "{0} {1} that originated from the United States.".format(matches1.group(1).replace(".", ""), matches1.group(2).replace(".", ""))

        instance["claim"] = new_claim

        return instance

    def name(self):
        return "american"


class LabelPreservingBirth1(ReplacementRule):
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


class LabelPreservingBirth2(ReplacementRule):
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


class LabelPreservingDeath1(ReplacementRule):
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


class LabelPreservingDeath2(ReplacementRule):
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


class LabelPreservingDeath3(ReplacementRule):
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



