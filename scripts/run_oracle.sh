#!/bin/bash
mkdir -pv data/model-specific/$MODEL/oracle/$1
mkdir -pv data/predictions/$MODEL/oracle/$1

if [ "$(wc -l < data/$1/$2)" -eq "$(wc -l < data/model-specific/$MODEL/oracle/$1/$2)" ];
then echo 'Skipping sampling evidence as this exists';
else
    python -m fever.evidence.negative_sample_nearest \
        --index data/index/fever-tfidf-ngram=2-hash=16777216-tokenizer=simple.npz \
        --in-file data/$1/$2 \
        --out-file data/model-specific/$MODEL/oracle/$1/$2
fi


if [ "$(wc -l < data/model-specific/$MODEL/oracle/$1/$2)" -eq "$(wc -l < data/predictions/$MODEL/oracle/$1/$2)" ];
then echo 'Skipping making predictions as this exists';
else
    python -m allennlp.run predict \
        $MODEL.tar.gz \
        data/model-specific/$MODEL/oracle/$1/$2 \
        --output-file data/predictions/$MODEL/oracle/$1/$2 \
        --predictor fever-oracle \
        --include-package fever.reader \
        --cuda-device -1 \
        --silent
fi;