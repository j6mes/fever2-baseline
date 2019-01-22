import json
import spacy

nlp = spacy.load('en_core_web_sm')

flatten = lambda l: [item for sublist in l for item in sublist]

with open("data/paper.dev.p5.s5.jsonl") as f:
    for row in f:
        line = json.loads(row)
        doc = nlp(line["claim"])
        all_evidence = flatten(line["evidence"])

        print(line["claim"])

        if line["label"] != "NOT ENOUGH INFO":

            np_chunks = [(noun_chunk, any([page_name in str(noun_chunk)
                                           for page_name in [evidence[2].replace("_", " ")
                            for evidence in all_evidence]]))
                         for noun_chunk in doc.noun_chunks]

            print(np_chunks)
            print(all_evidence)

        print("")
        print("")
