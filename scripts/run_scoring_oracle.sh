#!/bin/bash
export MODEL=fever-da
mkdir -pv data/submissions/$MODEL/oracle/$1

python src/experiment/score.py \
    --predicted_labels data/predictions/$MODEL/oracle/$1/$2 \
    --predicted_evidence data/model-specific/$MODEL/oracle/$1/$2 \
    --actual data/$1/$2
