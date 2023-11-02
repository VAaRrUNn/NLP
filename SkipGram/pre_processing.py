"""
Does all kinds of pre-processing to the dataset

- Loads the dataset using the prepare_sentecse.py
- Generates valid pairs for training (center_words, context_words, relation)
Also included sub-sampling, negative sampling, etc.
- Makes datasets and dataloaders.

To run this file:
execute in this fashion -> python -m nlp.skipgram.pre_processing.py
while you should be outside this nlp directory or it won't work.
"""



from nlp.utils import prepare_sentences
# from utils import prepare_sentences  # If prepare_sentences is a function
