from collections import Counter
from fever.reader.document_database import FEVERDocumentDatabase
from tqdm import tqdm
from nltk import ngrams
from multiprocessing import Pool
doc_db = FEVERDocumentDatabase("data/fever/fever.db")
doc_ids = doc_db.get_doc_ids()

counter = Counter()


def parse(id):

    lines = doc_db.get_doc_lines(id)
    sentences = [line.split("\t")[1] for line in lines if len(line.split("\t"))>1 and len(line.split("\t")[1])]

    for sentence in sentences:
        tokens = ("$START$ " + sentence + " $END$").split()
        bigrams = [" ".join(bigram) for bigram in ngrams(tokens,2)]
        counter.update(bigrams)
        counter.update(tokens)



p = Pool(10)
for _ in tqdm(p.imap_unordered(parse, doc_ids),total=len(doc_ids)):
    pass
