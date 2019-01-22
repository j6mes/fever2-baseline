import textwrap
import argparse
import numpy as np
from allennlp.data import Tokenizer, TokenIndexer
from allennlp.data.token_indexers import SingleIdTokenIndexer
from allennlp.models import load_archive
from fever.common.util.log_helper import LogHelper
from fever.retrieval.fever_doc_db import FeverDocDB
from fever.rte.parikh.reader import FEVERReader
from prettytable import PrettyTable
from evidence import EvidenceRetrieval


def process_line(method,line):
    sents = method.get_sentences_for_claim(line["claim"])
    pages = list(set(map(lambda sent:sent[0],sents)))
    line["predicted_pages"] = pages
    line["predicted_sentences"] = sents
    return line


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')



if __name__ == "__main__":
    LogHelper.setup()
    LogHelper.get_logger("allennlp.training.trainer")

    logger = LogHelper.get_logger(__name__)

    parser = argparse.ArgumentParser()
    parser.add_argument('--db', type=str, help='/path/to/saved/db.db')
    parser.add_argument('--drqa-model', type=str, help='/path/to/saved/db.db')
    parser.add_argument('--rte-model', type=str, help='/path/to/saved/db.db')
    parser.add_argument('--max-page',type=int,default=5)
    parser.add_argument('--max-sent',type=int,default=5)
    parser.add_argument("--cuda-device", type=int, default=-1, help='id of GPU to use (if any)')
    args = parser.parse_args()

    logger.info("Load DB")
    db = FeverDocDB(args.db)

    logger.info("Load RTE-Model")
    archive = load_archive(args.rte_model, cuda_device=args.cuda_device)

    logger.info("Init Retriever")
    evidence_retriever = EvidenceRetrieval(db, args.drqa_model, args.max_page, args.max_sent)

    config = archive.config
    ds_params = config["dataset_reader"]
    model = archive.model
    model.eval()

    reader = FEVERReader(db,     sentence_level=ds_params.pop("sentence_level",False),
                                 wiki_tokenizer=Tokenizer.from_params(ds_params.pop('wiki_tokenizer', {"word_splitter":{"type":"indexed_spaces"}})),
                                 claim_tokenizer=Tokenizer.from_params(ds_params.pop('claim_tokenizer',  {"word_splitter":{"type":"indexed_spaces"}})),
                                 token_indexers=TokenIndexer.dict_from_params(ds_params.pop('token_indexers', {'tokens': SingleIdTokenIndexer()})))



    print("")
    print("")
    print("")
    while True:
        claim = input("enter claim (or q to quit) >>\t")
        if claim.lower() == "q":
            break

        if len(claim.strip())<2:
            continue


        print("Pages:")
        pages = evidence_retriever.get_docs_for_claim(claim)
        tab = PrettyTable()

        tab.field_names = ["Page","Score"]
        for page,score in pages:
            tab.add_row((page,score))
        print(tab)

        evidence = evidence_retriever.get_sentences_for_claim(claim, include_text=True)
        print("Evidence:")
        tab = PrettyTable()
        tab.field_names = ["Page","Line","Sentence","Score"]
        for idx,sentence in enumerate(evidence):
            tab.add_row((sentence["page"],sentence["line_on_page"],textwrap.fill(sentence["sentence"],60),sentence["score"]))
        print(tab)

        sentences = [s["sentence"] for s in evidence]
        evidence = " ".join(sentences)
        item = reader.text_to_instance(evidence, claim)
        prediction = model.forward_on_instance(item, args.cuda_device)
        cls = model.vocab._index_to_token["labels"][np.argmax(prediction["label_probs"])]
        print("PREDICTED: {0}".format(cls))
        print()