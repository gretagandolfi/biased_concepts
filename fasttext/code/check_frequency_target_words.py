import re
import pickle
import gensim
from gensim.models.fasttext import FastText
from scipy.stats import spearmanr
from scipy import spatial
import numpy as np
import pandas as pd

model_path = '/Volumes/greta/models/model1.bin' 
#pretrained model (default parameters, 300 dimensions)
model1 = FastText.load_fasttext_format(model_path)


vocab = []

for k,v in model_dem.wv.vocab.items():
     vocab.append(k)
 
def divide_chunks(l, n): 
     for i in range(0, len(l), n):  
         yield l[i:i + n]

div = n_of_bins
x = list(divide_chunks(vocab, len(vocab)/div))


list_to_check = pickle.load(open(file_path, 'rb'))

yy = []
for j in list_to_check:
	y = []
	for i in range(0,div):
		if (re.sub(' ', '',j)).lower() in x[i]:
			y.append(i+1)
			if len(y) == 0:
				y.append(div+1)
	yy.append(y)
 

c = list
d = [i[0] for i in yy]
e = {'word': c, 'freq': d}
table = pd.DataFrame(e) 
  
#ee.to_csv('table.csv')


