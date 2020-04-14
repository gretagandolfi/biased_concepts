import re
import pickle
import gensim
from gensim.models.fasttext import FastText
from scipy.stats import spearmanr
from scipy import spatial
import numpy as np

model_path = '/Volumes/greta/models/model1.bin' 
#pretrained model (default parameters, 300 dimensions)

model1 = FastText.load_fasttext_format(model_path)

#the new corpus I want use to keep training. It is just tokenised, with no other preprocessing steps (list of sentences containing lists of tokens).
corpus_path = '/Users/gretagandolfi/Dropbox/thesis/progetto/fasttext/rep_aggiornato.pkl'
corpus = pickle.load(open(corpus_path, 'rb'))

#new training
model1.build_vocab(corpus, update=True)
model1.train(sentences=corpus, total_examples=len(corpus), epochs=model1.epochs)

#save the update model
model1.save('/Volumes/greta/models/model_rep/model_rep_up.bin')



