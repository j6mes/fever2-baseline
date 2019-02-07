import json
import argparse
from collections import Counter
from nltk.tokenize import PunktSentenceTokenizer
import nltk
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("--in-file", type=str)
args = parser.parse_args()


claims = []

bigrams = Counter()

with open(args.in_file) as f:
    for line in tqdm(f):
        line = json.loads(line)

        claims.append(line["claim"])

tok = PunktSentenceTokenizer()
for claim in tqdm(claims):
    bigrams.update(nltk.bigrams(nltk.word_tokenize(claim)))

for bigram in bigrams.most_common(20):
    print(bigram)
