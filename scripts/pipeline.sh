#!/bin/bash
mkdir -pv data/pipeline/$MODEL

if [ "$(wc -l < data/generate/$1)" -eq "$(wc -l < data/pipeline/$MODEL/full.$1)" ];
then echo 'Skipping sampling evidence as this exists';
else
python -m fever.evidence.retrieve \
    --index data/index/fever-tfidf-ngram=2-hash=16777216-tokenizer=simple.npz \
    --database data/fever/fever.db \
    --in-file data/$1 \
    --out-file data/pipeline/$MODEL/full.ir.$1 \
    --max-page 5 \
    --max-sent 5
fi

if [ "$(wc -l < data/pipeline/$MODEL/full.ir.$1 )" -eq "$(wc -l < data/pipeline/$MODEL/full.predictions.$1)" ];
then echo 'Skipping making predictions as this exists';
else
    python -m allennlp.run predict \
        $MODEL.tar.gz \
        data/pipeline/$MODEL/full.ir.$1 \
        --output-file data/pipeline/$MODEL/full.predictions.$1 \
        --predictor fever \
        --include-package fever.reader \
        --cuda-device -1 \
        --silent
fi