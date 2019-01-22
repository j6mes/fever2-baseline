from typing import Dict, Optional

import torch
from allennlp.data import Vocabulary
from allennlp.models.model import Model
from allennlp.modules import TextFieldEmbedder, FeedForward, Seq2VecEncoder
from allennlp.nn import InitializerApplicator, RegularizerApplicator
from allennlp.nn.util import get_text_field_mask
from allennlp.training.metrics import CategoricalAccuracy
from overrides import overrides


@Model.register("fevercheck")
class FeverCheckModel(Model):

    def __init__(self, vocab: Vocabulary,
                 embeddings:TextFieldEmbedder,
                 project:FeedForward,
                 encoder:Seq2VecEncoder,
                 classifier:FeedForward,
                 initializer: InitializerApplicator = InitializerApplicator(),
                 regularizer: Optional[RegularizerApplicator] = None):
        super().__init__(vocab, regularizer)
        self.embeddings = embeddings
        self.project = project
        self.encoder = encoder
        self.classifier = classifier

        self._accuracy = CategoricalAccuracy()
        self._loss = torch.nn.CrossEntropyLoss()

        initializer(self)


    @overrides
    def forward(self,
                tokens: Dict[str,torch.LongTensor],
                label: torch.IntTensor = None):
        embedded = self.embeddings(tokens)

        mask = get_text_field_mask(tokens)
        projected = self.project(embedded)

        encoded = self.encoder(projected, mask)

        predicted_logits = self.classifier(encoded)
        predicted_probs = torch.nn.functional.softmax(predicted_logits, dim=-1)
        output_dict = {"logits":predicted_logits, "probs":predicted_probs}

        if label is not None:
            loss = self._loss(predicted_logits, label.long())
            self._accuracy(predicted_logits, label)
            output_dict["loss"] = loss

        return output_dict


    def get_metrics(self, reset:bool=False):
        return {"accuracy": self._accuracy.get_metric(reset)}