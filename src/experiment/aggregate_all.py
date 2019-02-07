from argparse import ArgumentParser
from pathlib import Path
import re
import os
from shutil import copyfile
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


os.makedirs(args.predicted_labels_dir+"/oracle/all",exist_ok=True)
os.makedirs(args.predicted_labels_dir+"/full/all",exist_ok=True)

os.makedirs(args.predicted_evidence_dir +"/oracle/all",exist_ok=True)
os.makedirs(args.predicted_evidence_dir +"/full/all",exist_ok=True)

os.makedirs(args.actual_dir +"/all",exist_ok=True)


for experiment_path in experiments:
    matches = re.match(r'/([a-z-]+)/([a-z-]+).(.+).jsonl',experiment_path)
    experiment = str(matches.group(3))

    print(experiment)


    changed_oracle_new_predicted_file = args.predicted_labels_dir + "/oracle/all/changed." + family + "." + experiment + ".jsonl"
    changed_oracle_new_evidence_file = args.predicted_evidence_dir + "/oracle/all/changed." + family + "." + experiment + ".jsonl"
    changed_full_new_predicted_file = args.predicted_labels_dir + "/full/all/changed." + family + "." + experiment + ".jsonl"
    changed_full_new_evidence_file = args.predicted_evidence_dir + "/full/all/changed." + family + "." + experiment + ".jsonl"
    changed_new_actual_file = args.actual_dir + "/all/changed." + family + "." + experiment + ".jsonl"

    unchanged_oracle_new_predicted_file = args.predicted_labels_dir + "/oracle/all/unchanged."+family+"."+experiment + ".jsonl"
    unchanged_oracle_new_evidence_file = args.predicted_evidence_dir + "/oracle/all/unchanged." +family+"."+ experiment + ".jsonl"
    unchanged_full_new_predicted_file = args.predicted_labels_dir + "/full/all/unchanged."+family+"."+experiment + ".jsonl"
    unchanged_full_new_evidence_file = args.predicted_evidence_dir + "/full/all/unchanged." +family+"."+ experiment + ".jsonl"
    unchanged_new_actual_file = args.actual_dir + "/all/unchanged." +family+"."+ experiment + ".jsonl"


    unchanged_oracle_old_predicted_file = args.predicted_labels_dir + "/oracle/" + family + "/unchanged." + experiment + ".jsonl"
    unchanged_oracle_old_evidence_file = args.predicted_evidence_dir + "/oracle/" + family + "/unchanged." + experiment + ".jsonl"
    unchanged_old_actual_file = args.actual_dir + "/" + family + "/unchanged." + experiment + ".jsonl"

    changed_oracle_old_predicted_file = args.predicted_labels_dir + "/oracle/" + family + "/changed." + experiment + ".jsonl"
    changed_oracle_old_evidence_file = args.predicted_evidence_dir + "/oracle/" + family + "/changed." + experiment + ".jsonl"
    changed_old_actual_file = args.actual_dir + "/" + family + "/changed." + experiment + ".jsonl"

    unchanged_full_old_predicted_file = args.predicted_labels_dir + "/full/" + family + "/unchanged." + experiment + ".jsonl"
    unchanged_full_old_evidence_file = args.predicted_evidence_dir + "/full/" + family + "/unchanged." + experiment + ".jsonl"
    changed_full_old_predicted_file = args.predicted_labels_dir + "/full/" + family + "/changed." + experiment + ".jsonl"
    changed_full_old_evidence_file = args.predicted_evidence_dir + "/full/" + family + "/changed." + experiment + ".jsonl"



    try:
        copyfile(unchanged_oracle_old_predicted_file, unchanged_oracle_new_predicted_file)
        copyfile(unchanged_oracle_old_evidence_file, unchanged_oracle_new_evidence_file)

        copyfile(changed_oracle_old_predicted_file, changed_oracle_new_predicted_file)
        copyfile(changed_oracle_old_evidence_file, changed_oracle_new_evidence_file)
    except:
        print("Could not copy oracle data for " + experiment)

    copyfile(unchanged_old_actual_file, unchanged_new_actual_file)
    copyfile(unchanged_full_old_predicted_file, unchanged_full_new_predicted_file)
    copyfile(unchanged_full_old_evidence_file, unchanged_full_new_evidence_file)
    copyfile(changed_old_actual_file, changed_new_actual_file)
    copyfile(changed_full_old_predicted_file, changed_full_new_predicted_file)
    copyfile(changed_full_old_evidence_file, changed_full_new_evidence_file)