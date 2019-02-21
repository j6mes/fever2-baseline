#!/usr/bin/env bash


# Generate all claims
PYTHONPATH=src python src/claim_rewriter.py --in-file data/fever-data/dev.jsonl --out-file data/meaning-preserving-dev
PYTHONPATH=src python src/claim_rewriter2.py --in-file data/fever-data/dev.jsonl --out-file data/simple-negate-dev
PYTHONPATH=src python src/claim_rewriter3.py --in-file data/fever-data/dev.jsonl --out-file data/complex-negate-dev

PYTHONPATH=src python src/claim_rewriter.py --in-file data/fever-data/test.jsonl --out-file data/meaning-preserving-test
PYTHONPATH=src python src/claim_rewriter2.py --in-file data/fever-data/test.jsonl --out-file data/simple-negate-test
PYTHONPATH=src python src/claim_rewriter3.py --in-file data/fever-data/test.jsonl --out-file data/complex-negate-test

# Get list of all generated claims for final eval
mkdir -pv data/generated
cat data/meaning-preserving-dev/changed.* data/simple-negate-dev/changed.* data/complex-negate-dev/changed.* > data/generated/dev.everything.jsonl
cat data/meaning-preserving-test/changed.* data/simple-negate-test/changed.* data/complex-negate-test/changed.* > data/generated/test.everything.jsonl

# Sample 1000 claims uniformly at random from the test set
PYTHONPATH=src python src/experiment/sampling.py --in-file data/fever-data/dev.jsonl --out-file data/generated/dev.sampled.1000.jsonl --size 1000
PYTHONPATH=src python src/experiment/sampling.py --in-file data/fever-data/test.jsonl --out-file data/generated/test.sampled.1000.jsonl --size 1000
cp data/generated/dev.sampled.1000.jsonl data/
cp data/generated/test.sampled.1000.jsonl data/
bash scripts/pipeline.sh dev.sampled.1000.jsonl
bash scripts/pipeline.sh test.sampled.1000.jsonl

# Just look at generated claims
PYTHONPATH=src python src/experiment/sampling.py --in-file data/generated/dev.everything.jsonl --out-file data/generated/dev.uniform.1000.jsonl --size 1000
PYTHONPATH=src python src/experiment/sampling.py --in-file data/generated/test.everything.jsonl --out-file data/generated/test.uniform.1000.jsonl --size 1000
cp data/generated/dev.uniform.1000.jsonl data/
cp data/generated/test.uniform.1000.jsonl data/
bash scripts/pipeline.sh dev.uniform.1000.jsonl
bash scripts/pipeline.sh test.uniform.1000.jsonl


mkdir -pv data/sample_submission/uniform-dev
mkdir -pv data/sample_submission/uniform-test
python -m fever.submission.prepare --predicted_labels data/pipeline/fever-da/full.predictions.dev.uniform.1000.jsonl --predicted_evidence data/pipeline/fever-da/full.ir.dev.uniform.1000.jsonl --out_file data/sample_submission/random-dev/fever-da.jsonl
python -m fever.submission.prepare --predicted_labels data/pipeline/fever-da/full.predictions.test.uniform.1000.jsonl --predicted_evidence data/pipeline/fever-da/full.ir.test.uniform.1000.jsonl --out_file data/sample_submission/random-test/fever-da.jsonl
python -m fever.submission.prepare --predicted_labels data/pipeline/fever-esim-elmo/full.predictions.dev.uniform.1000.jsonl --predicted_evidence data/pipeline/fever-esim-elmo/full.ir.dev.uniform.1000.jsonl --out_file data/sample_submission/random-dev/fever-esim-elmo.jsonl
python -m fever.submission.prepare --predicted_labels data/pipeline/fever-esim-elmo/full.predictions.test.uniform.1000.jsonl --predicted_evidence data/pipeline/fever-esim-elmo/full.ir.test.uniform.1000.jsonl --out_file data/sample_submission/random-test/fever-esim-elmo.jsonl
cp /local/scratch-2/jt719/combine-FEVER-NSMN/fever2/predictions/unc/full/final/dev.uniform.1000.jsonl data/sample_submission/random-dev/unc.jsonl
cp /local/scratch-2/jt719/combine-FEVER-NSMN/fever2/predictions/unc/full/final/test.uniform.1000.jsonl data/sample_submission/random-test/unc.jsonl




python -m fever2.scorer --actual-file data/generated/dev.sampled.1000.jsonl --submission-dir data/sample_submission/sampled-dev/
python -m fever2.scorer --actual-file data/generated/test.sampled.1000.jsonl --submission-dir data/sample_submission/sampled-test/
python -m fever2.scorer --actual-file data/generated/dev.uniform.1000.jsonl --submission-dir data/sample_submission/random-dev/
python -m fever2.scorer --actual-file data/generated/test.uniform.1000.jsonl --submission-dir data/sample_submission/random-test/



for i in $(seq 1 10)
do
    PYTHONPATH=src RANDOM_SEED=$i python src/experiment/sampling.py --in-file data/fever-data/dev.jsonl --out-file data/generated/dev.sampled.$i.1000.jsonl --size 500
    PYTHONPATH=src RANDOM_SEED=$i python src/experiment/sampling.py --in-file data/fever-data/test.jsonl --out-file data/generated/test.sampled.$i.1000.jsonl --size 500
    cp data/generated/dev.sampled.$i.1000.jsonl data/
    cp data/generated/test.sampled.$i.1000.jsonl data/
    cp data/generated/dev.sampled.$i.1000.jsonl /local/scratch-2/jt719/combine-FEVER-NSMN/fever2/final/
    cp data/generated/test.sampled.$i.1000.jsonl /local/scratch-2/jt719/combine-FEVER-NSMN/fever2/final/
done

for i in $(seq 1 10)
do
    export MODEL=fever-da
    bash scripts/pipeline.sh dev.sampled.$i.1000.jsonl
    bash scripts/pipeline.sh test.sampled.$i.1000.jsonl
    export MODEL=fever-esim-elmo
    bash scripts/pipeline.sh dev.sampled.$i.1000.jsonl
    bash scripts/pipeline.sh test.sampled.$i.1000.jsonl
    mkdir -pv data/sample_submission/sampled-dev.$i
    mkdir -pv data/sample_submission/sampled-test.$i
    python -m fever.submission.prepare --predicted_labels data/pipeline/fever-da/full.predictions.dev.sampled.$i.1000.jsonl --predicted_evidence data/pipeline/fever-da/full.ir.dev.sampled.$i.1000.jsonl --out_file data/sample_submission/sampled-dev.$i/fever-da.jsonl
    python -m fever.submission.prepare --predicted_labels data/pipeline/fever-da/full.predictions.test.sampled.$i.1000.jsonl --predicted_evidence data/pipeline/fever-da/full.ir.test.sampled.$i.1000.jsonl --out_file data/sample_submission/sampled-test.$i/fever-da.jsonl
    python -m fever.submission.prepare --predicted_labels data/pipeline/fever-esim-elmo/full.predictions.dev.sampled.$i.1000.jsonl --predicted_evidence data/pipeline/fever-esim-elmo/full.ir.dev.sampled.$i.1000.jsonl --out_file data/sample_submission/sampled-dev.$i/fever-esim-elmo.jsonl
    python -m fever.submission.prepare --predicted_labels data/pipeline/fever-esim-elmo/full.predictions.test.sampled.$i.1000.jsonl --predicted_evidence data/pipeline/fever-esim-elmo/full.ir.test.sampled.$i.1000.jsonl --out_file data/sample_submission/sampled-test.$i/fever-esim-elmo.jsonl
    cp /local/scratch-2/jt719/combine-FEVER-NSMN/fever2/predictions/unc/full/final/dev.sampled.$i.1000.jsonl data/sample_submission/sampled-dev.$i/unc.jsonl
    cp /local/scratch-2/jt719/combine-FEVER-NSMN/fever2/predictions/unc/full/final/test.sampled.$i.1000.jsonl data/sample_submission/sampled-test.$i/unc.jsonl
    echo "Welcome $i times"
done

for i in $(seq 1 10)
do
    bash scripts/predict.sh final dev.sampled.$i.1000.jsonl;
    bash scripts/predict.sh final test.sampled.$i.1000.jsonl;
done








mkdir -pv data/sample_submission/sampled-dev
mkdir -pv data/sample_submission/sampled-test
python -m fever.submission.prepare --predicted_labels data/pipeline/fever-da/full.predictions.dev.sampled.1000.jsonl --predicted_evidence data/pipeline/fever-da/full.ir.dev.sampled.1000.jsonl --out_file data/sample_submission/sampled-dev/fever-da.jsonl
python -m fever.submission.prepare --predicted_labels data/pipeline/fever-da/full.predictions.test.sampled.1000.jsonl --predicted_evidence data/pipeline/fever-da/full.ir.test.sampled.1000.jsonl --out_file data/sample_submission/sampled-test/fever-da.jsonl
python -m fever.submission.prepare --predicted_labels data/pipeline/fever-esim-elmo/full.predictions.dev.sampled.1000.jsonl --predicted_evidence data/pipeline/fever-esim-elmo/full.ir.dev.sampled.1000.jsonl --out_file data/sample_submission/sampled-dev/fever-esim-elmo.jsonl
python -m fever.submission.prepare --predicted_labels data/pipeline/fever-esim-elmo/full.predictions.test.sampled.1000.jsonl --predicted_evidence data/pipeline/fever-esim-elmo/full.ir.test.sampled.1000.jsonl --out_file data/sample_submission/sampled-test/fever-esim-elmo.jsonl
cp /local/scratch-2/jt719/combine-FEVER-NSMN/fever2/predictions/unc/full/final/dev.sampled.1000.jsonl data/sample_submission/sampled-dev/unc.jsonl
cp /local/scratch-2/jt719/combine-FEVER-NSMN/fever2/predictions/unc/full/final/test.sampled.1000.jsonl data/sample_submission/sampled-test/unc.jsonl


