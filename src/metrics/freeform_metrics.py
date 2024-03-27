import torch

from itertools import chain, combinations
from transformers import AutoTokenizer, AutoModel


class CoherenceEvaluator:

    def __init__(self, nli_model_checkpoint='sentence-transformers/nli-bert-base'):
        """ CoherenceEvaluator constructor."""
        self.tokenizer = AutoTokenizer.from_pretrained(nli_model_checkpoint)
        self.model = AutoModel.from_pretrained(nli_model_checkpoint)
        self.model.eval()


    def contr(self, prop_a, prob_b):
        inputs = self.tokenizer([prop_a, prob_b], padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            score = self.model(**inputs).logits
            label_mapping = ['contradiction', 'entailment', 'neutral']
            labels = [label_mapping[score_max] for score_max in score.argmax(dim=1)]

        return True if labels[0] == 'contradiction' else False

    def coherence_metric(self, props, y_hat):
        """Compute the coherence metric for a free form explanation."""
        all_subsets = chain.from_iterable(combinations(range(len(props)), r)
                                          for r in range(len(props) + 1))

        num_props = len(props)
        coherent_props = 0
        X = [x for x in props if x != y_hat]

        for props_prime in all_subsets:
            not_contr_props_y = ~self.contr(props_prime, y_hat)
            not_contr_props_X = ~self.contr(props_prime, X)
            coherent_props += not_contr_props_y * not_contr_props_X

        return coherent_props / num_props





