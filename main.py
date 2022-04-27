# pip install sklearn
# pip install nltk

import pandas as pd
from models import OnlyInA, TF_IDF, Binary_weight

dataset_true = pd.read_csv('./data/True.csv', usecols=['title', 'text'])  # Read file
dataset_fake = pd.read_csv('./data/Fake.csv', usecols=['title', 'text'])

sample_true = dataset_true['title']  # Take a sample of data
sample_fake = dataset_fake['title']

# OnlyInA.onlyInA(sample_true, sample_fake, "Top10 tokens only in True message", "top10_true")
# OnlyInA.onlyInA(sample_fake, sample_true, "Top10 tokens only in Fake message", "top10_fake")
TF_IDF.TF_IDF(sample_fake, "Key tokens in Fake message based on TD-IDF", "TD-IDF_fake")
# Binary_weight.Binary_weight(sample_fake, "Crucial tokens in Fake message based on binary weight", "binary_weight_Fake")

