import torch

from score import Scorer
from itertools import chain, combinations
from transformers import AutoTokenizer, AutoModel


class CoherenceEvaluator:

    def __init__(self, nli_model_checkpoint='sentence-transformers/nli-bert-base'):
        """ CoherenceEvaluator constructor."""
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained(nli_model_checkpoint)
        self.model = AutoModel.from_pretrained(nli_model_checkpoint)
        self.model.eval()

    def coherence_metric(self, propositions, y_hat):
        """Compute the coherence metric for a free form explanation."""
        all_subsets = chain.from_iterable(combinations(range(len(props)), r)
                                          for r in range(len(props) + 1))

        num_props = len(propositions)
        coherent_props = 0
        rationales = [x for x in propositions if x != y_hat]

        for props_prime in all_subsets:
            not_contr_props_y = ~self._is_contradiction(props_prime, y_hat)
            not_contr_props_X = ~self._is_contradiction(props_prime, rationales)
            coherent_props += not_contr_props_y * not_contr_props_X

        return coherent_props / num_props

    def _is_contradiction(self, prop_a, prob_b):
        """Use NLI model to predict the relation between rationales prob_a and prob_b."""

        inputs = self.tokenizer([prop_a, prob_b], padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            score = self.model(**inputs).logits
            label_mapping = ['contradiction', 'entailment', 'neutral']
            labels = [label_mapping[score_max] for score_max in score.argmax(dim=1)]

        return True if labels[0] == 'contradiction' else False
