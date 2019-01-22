import json
import random
from copy import deepcopy
from typing import Dict

import numpy as np
from allennlp.data import DatasetReader, Tokenizer, TokenIndexer, Instance
from allennlp.data.fields import TextField, LabelField
from allennlp.data.token_indexers import SingleIdTokenIndexer
from allennlp.data.tokenizers import WordTokenizer
from allennlp.nn import Initializer, InitializerApplicator
from fever.scorer import evidence_macro_recall, is_correct_label
from overrides import overrides
from tqdm import tqdm


@DatasetReader.register("error-check")
class ErrorCheckDatasetReader(DatasetReader):

    def __init__(self,
                 tokenizer: Tokenizer = None,
                 token_indexers: Dict[str, TokenIndexer] = None):
        super().__init__()
        self._tokenizer = tokenizer or WordTokenizer()
        self._token_indexers = token_indexers or {"tokens":SingleIdTokenIndexer()}

        def load_predictions(file):
            predictions = []

            evaluate_instances = []
            all_instances = []

            with open(file) as file:
                for line in file:
                    predictions.append(json.loads(line))

            for idx, instance in enumerate(public_data):
                instance = deepcopy(instance)

                instance["predicted_label"] = predictions[idx]["predicted_label"]
                instance["predicted_evidence"] = predictions[idx]["predicted_evidence"]

                instance["label"] = actual_data[idx]["label"]
                instance["evidence"] = actual_data[idx]["evidence"]

                all_instances.append(instance)

                if evidence_macro_recall(instance)[0] < evidence_macro_recall(instance)[1]:
                    #evaluate_instances.append(instance)
                    pass

                if is_correct_label(instance):
                    # print("Correct label")
                    pass
                else:
                    if evidence_macro_recall(instance)[0] >= 1.0:
                        #pass
                        evaluate_instances.append(instance)

            return evaluate_instances, all_instances

        public_data = []

        with open("data/gold/blind_public.jsonl") as file:
            for line in file:
                public_data.append(json.loads(line))

        actual_data = []

        with open("data/gold/blind_private.jsonl") as file:
            for line in file:
                actual_data.append(json.loads(line))

        pos_insts = []
        all_insts = []

        a, b = load_predictions("data/submission/predictions_1.jsonl")
        pos_insts.extend(a)
        all_insts.extend(b)

        a, b = load_predictions("data/submission/predictions_2.jsonl")
        pos_insts.extend(a)
        all_insts.extend(b)

        claim_ids = {i: 1 for i in (map(lambda instance: instance["id"], pos_insts))}.keys()
        sample_pool = list(filter(lambda instance: instance["id"] not in claim_ids, all_insts))

        sample_ids = np.random.choice(len(sample_pool), size=len(pos_insts), replace=False)
        negative_examples = list(map(lambda id: sample_pool[id], sample_ids))

        all_labels = ["FAIL"] * len(pos_insts) + ["PASS"] * len(negative_examples)
        all_data = pos_insts + negative_examples

        mixed = list(zip(all_data, all_labels))
        random.shuffle(mixed)

        self.mixed = mixed


    @overrides
    def text_to_instance(self, claim, label) -> Instance:
        claim_tokens = self._tokenizer.tokenize(claim)
        return Instance({"tokens":TextField(claim_tokens, self._token_indexers),
                         "label": LabelField(label)})

    @overrides
    def _read(self, file_path:str):

        mixed_train = self.mixed[:len(self.mixed) // 2]
        mixed_dev = self.mixed[:len(self.mixed) // 2]

        if file_path == "train":
            return [self.text_to_instance(item[0]['claim'],item[1]) for item in mixed_train]
        elif file_path == "dev":
            return [self.text_to_instance(item[0]['claim'],item[1]) for item in mixed_dev]
        return None

