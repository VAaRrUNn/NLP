"""
Does all kinds of pre-processing to the dataset

- Loads the dataset using the prepare_sentecse.py
- Generates valid pairs for training (center_words, context_words, relation)
Also included sub-sampling, negative sampling, etc.
- Makes datasets and dataloaders.
"""



from ..utils import prepare_sentences
# from utils import prepare_sentences  # If prepare_sentences is a function
