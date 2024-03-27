# Evaluating Explanations
Implementation of evaluation metrics introduced in COLING-LREC 2024 paper.



## Getting Started

```commandline
conda create -n evaluate_explanations python=3.10
conda activate evaluate_explanations
pip install -r requirements.txt
```

## Using metrics

In order to use the metrics defined in this repository add the following line to your python script
```python 
   from src.metrics import argumentative_metrics, deductive_metrics, freeform_metrics
```


## Reference

If you use the dataset, please cite the paper as formatted below.

```
@inproceedings{kotonya-toni-2024-evaluating-explanations,
    title = "Towards a Framework for Evaluating Explanations in Automated Fact Verification",
    author = "Kotonya, Neema  and Toni, Francesca",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
}
```

## Contact

Please feel free to contact [Neema Kotonya](mailto:nk2418@ic.ac.uk) if you have any queries.