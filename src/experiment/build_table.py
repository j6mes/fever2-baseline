import argparse
import json
import sys
from fever.scorer import fever_score
from prettytable import PrettyTable

parser = argparse.ArgumentParser()
parser.add_argument("--predicted-labels-dir",type=str)
parser.add_argument("--predicted-evidence-dir",type=str, default=None)
parser.add_argument("--actual-dir",type=str)
parser.add_argument("--family",type=str)

args = parser.parse_args()
family = args.family
from pathlib import Path

experiments = []
pathlist = Path(args.actual_dir+"/"+family).glob('*.jsonl')
for path in pathlist:
    path_in_str = str(path)
    experiments.append(path_in_str.replace(args.actual_dir,""))

def score_submission(predicted_labels_file, predicted_evidence_file, actual_labels_file):
    predicted_labels =[]
    predicted_evidence = []
    actual = []

    flatten = lambda l: [item for sublist in l for item in sublist]

    with open(predicted_labels_file,"r") as predictions_file:
        for line in predictions_file:
            predicted_labels.append(json.loads(line)["predicted_label"])

    with open(actual_labels_file, "r") as actual_file:
        for line in actual_file:
            actual.append(json.loads(line))

    with open(predicted_evidence_file, "r") as predictions_file:
        for line in predictions_file:
            line = json.loads(line)

            if "predicted_evidence" in line:
                predicted_evidence.append(line["predicted_evidence"])
            elif "predicted_sentences" in line:
                predicted_evidence.append(line["predicted_sentences"])
            else:
                predicted_evidence.append([[e[2],e[3]] for e in flatten(line["evidence"])])


    predictions = []


    for ev,label in zip(predicted_evidence,predicted_labels):
        predictions.append({"predicted_evidence":ev,"predicted_label":label})

    sdata = list(fever_score(predictions,actual))
    sdata.append(len(predictions))
    return tuple(sdata)


tab = PrettyTable()
tab.field_names = ["Model", "Number of Data", "Oracle Accuracy Before", "Oracle Accuracy After","Delta Oracle Accuracy",
                   "Pipeline Accuracy Before", "Pipeline Accuracy After", "Delta Pipeline Accuracy",
                   "Pipeline FEVER Score Before", "Pipeline FEVER Score After","Delta FEVER Score Accuracy"
                   ]

paired_expts = set()
for experiment in experiments:
    paired_expts.add(experiment.replace("unchanged.","").replace("changed.","").replace(".jsonl","").replace("/","").replace(family,""))


for experiment in paired_expts:
    try:
        try:
            oracle_score_before,oracle_acc_before,_,_,_ ,_= score_submission(args.predicted_labels_dir+"/oracle/"+family+"/unchanged."+experiment + ".jsonl",
                                                             args.predicted_evidence_dir + "/oracle/"+family+"/unchanged." + experiment + ".jsonl",
                                                             args.actual_dir +"/" +family+"/unchanged." + experiment + ".jsonl",
                                                             )
            oracle_score_after,oracle_acc_after,_,_,_,_ = score_submission(args.predicted_labels_dir+"/oracle/"+family+"/changed."+experiment + ".jsonl",
                                                             args.predicted_evidence_dir + "/oracle/"+family+"/changed." + experiment + ".jsonl",
                                                             args.actual_dir +"/" +family+"/changed." + experiment + ".jsonl",
                                                             )
        except:
            oracle_score_before = 0
            oracle_acc_before = 0

            oracle_score_after = 0
            oracle_acc_after = 0


        full_score_before,full_acc_before,_,_,_ ,_= score_submission(args.predicted_labels_dir+"/full/"+family+"/unchanged."+experiment + ".jsonl",
                                                         args.predicted_evidence_dir + "/full/"+family+"/unchanged." + experiment + ".jsonl",
                                                         args.actual_dir  +"/"+family+"/unchanged." + experiment + ".jsonl",
                                                         )
        full_score_after,full_acc_after,_,_,_,elen = score_submission(args.predicted_labels_dir+"/full/"+family+"/changed."+experiment + ".jsonl",
                                                         args.predicted_evidence_dir + "/full/"+family+"/changed." + experiment + ".jsonl",
                                                         args.actual_dir +"/"+family+"/changed." + experiment + ".jsonl",
                                                         )


        tab.add_row([experiment,elen,
                     "%.2f"%(round(oracle_score_before*100,4)), "%.2f"%(round(oracle_score_after*100,4)), "%.2f"%(round((oracle_score_after-oracle_score_before)*100,4)),
                     "%.2f"%(round(full_acc_before*100,4)), "%.2f"%(round(full_acc_after*100,4)), "%.2f"%(round(( full_acc_after-full_acc_before)*100,4)),
                     "%.2f"%(round(full_score_before*100,4)), "%.2f"%(round(full_score_after*100,4)), "%.2f"%(round((full_score_after-full_score_before)*100,4))
                 ])

    except Exception as e:
        print(e)
        raise e

print(tab)