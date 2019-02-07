from argparse import ArgumentParser
from pathlib import Path
import re
parser = ArgumentParser()

parser.add_argument("--family",type=str)
parser.add_argument("--predicted-labels-dir",type=str)
parser.add_argument("--predicted-evidence-dir",type=str)
parser.add_argument("--actual-dir",type=str)
args = parser.parse_args()

family = args.family

experiments = []
pathlist = Path(args.actual_dir+"/"+family).glob('*.jsonl')
for path in pathlist:
    path_in_str = str(path)
    experiments.append(path_in_str.replace(args.actual_dir,""))


for experiment_path in experiments:
    matches = re.match(r'/([a-z-]+)/([a-z-]+).(.+).jsonl',experiment_path)
    experiment = matches.group(3)

    print(experiment)


    changed_oracle_new_predicted_file = args.predicted_labels_dir + "/oracle/all/changed." + family + "." + experiment + ".jsonl"
    changed_oracle_new_evidence_file = args.predicted_evidence_dir + "/oracle/all/changed." + family + "." + experiment + ".jsonl"
    changed_full_new_predicted_file = args.predicted_labels_dir + "/full/all/changed." + family + "." + experiment + ".jsonl"
    changed_full_new_evidence_file = args.predicted_evidence_dir + "/full/all/changed." + family + "." + experiment + ".jsonl"
    changed_new_actual_file = args.actual_dir + "/all/unchanged." + family + "." + experiment + ".jsonl"

    unchanged_oracle_new_predicted_file = args.predicted_labels_dir + "/oracle/all/unchanged."+family+"."+experiment + ".jsonl"
    unchanged_oracle_new_evidence_file = args.predicted_evidence_dir + "/oracle/all/unchanged." +family+"."+ experiment + ".jsonl"
    unchanged_full_new_predicted_file = args.predicted_labels_dir + "/full/all/unchanged."+family+"."+experiment + ".jsonl"
    unchanged_full_new_evidence_file = args.predicted_evidence_dir + "/full/all/unchanged." +family+"."+ experiment + ".jsonl"
    unchanged_new_actual_file = args.actual_dir + "/all/unchanged." +family+"."+ experiment + ".jsonl"


