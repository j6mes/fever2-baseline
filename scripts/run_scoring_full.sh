#!/bin/bash
export MODEL=fever-da
mkdir -pv data/submissions/$MODEL/full/$1/

python src/experiment/score.py \
    --predicted_labels data/predictions/$MODEL/full/$1/$2 \
    --predicted_evidence data/model-specific/$MODEL/full/$1/$2 \
    --actual data/$1/$2
