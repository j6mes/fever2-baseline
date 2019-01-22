#!/bin/bash
export MODEL=fever-da
mkdir -pv data/model-specific/$MODEL/oracle/$1
mkdir -pv data/predictions/$MODEL/oracle/$1

python -m fever.evidence.negative_sample_nearest \
    --index data/index/fever-tfidf-ngram=2-hash=16777216-tokenizer=simple.npz \
    --in-file data/$1/$2 \
    --out-file data/model-specific/$MODEL/oracle/$1/$2

python -m allennlp.run predict \
    model.tar.gz \
    data/model-specific/$MODEL/oracle/$1/$2 \
    --output-file data/predictions/$MODEL/oracle/$1/$2 \
    --predictor fever-oracle \
    --include-package fever.reader \
    --cuda-device -1 \
    --silent
