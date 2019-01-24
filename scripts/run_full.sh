#!/bin/bash
mkdir -pv data/model-specific/$MODEL/full/$1
mkdir -pv data/predictions/$MODEL/full/$1

if [ "$(wc -l < data/$1/$2)" -eq "$(wc -l < data/model-specific/$MODEL/full/$1/$2)" ];
then echo 'Skipping sampling evidence as this exists';
else
python -m fever.evidence.retrieve \
    --index data/index/fever-tfidf-ngram=2-hash=16777216-tokenizer=simple.npz \
    --database data/fever/fever.db \
    --in-file data/$1/$2 \
    --out-file data/model-specific/$MODEL/full/$1/$2 \
    --max-page 5 \
    --max-sent 5
fi

if [ "$(wc -l < data/model-specific/$MODEL/full/$1/$2)" -eq "$(wc -l < data/predictions/$MODEL/full/$1/$2)" ];
then echo 'Skipping making predictions as this exists';
else
    python -m allennlp.run predict \
        $MODEL.tar.gz \
        data/model-specific/$MODEL/full/$1/$2 \
        --output-file data/predictions/$MODEL/full/$1/$2 \
        --predictor fever \
        --include-package fever.reader \
        --cuda-device -1 \
        --silent
fi