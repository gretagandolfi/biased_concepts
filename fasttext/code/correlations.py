import re
import pickle
import gensim
from gensim.models.fasttext import FastText
from scipy.stats import spearmanr
from scipy import spatial
import numpy

#In SimLex-99 txt file, I removed the names of the columns, and I replaced every 'A' with 0.

#correlation with SimLex
def correlates_SIM(model): 
	sim = open('/Users/gretagandolfi/Dropbox/thesis/progetto/corpus/SimLex-999/SimLex-999.txt', 'r')
	voc = {}
	system = []
	gold = []
	for l in sim:
		fields = l.rstrip().split('\t')
		w1 = fields[0].replace("-n",".n")    
		w2 = fields[1].replace("-n",".n")
		score = float(fields[3])
		try:
			voc[w1] = model.wv[w1]
		except KeyError:
			voc[w1] = np.random.rand()
			print(w1)
		try:
			voc[w2] = model.wv[w2]
		except KeyError:
			voc[w2] = np.random.rand()
			print(w2)
          
		cos = 1 - spatial.distance.cosine(voc.get(w1),voc.get(w2))
		system.append(cos)
		gold.append(score)
  
	sim.close()
	return spearmanr(system, gold).correlation

# MEN dataset correlation
def correlates(model): 
     sim = open('/Users/gretagandolfi/Dropbox/thesis/progetto/corpus/MEN/MEN_dataset_natural_form_full.txt', 'r')
     voc = {}
     system = []
     gold = []
     for l in sim:
                     fields = l.rstrip('\n').split()
                     w1 = fields[0].replace("-n",".n")    
                     w2 = fields[1].replace("-n",".n")
                     score = float(fields[2])
                     try:
                     	voc[w1] = model.wv[w1]
                     except KeyError:
                     	voc[w1] = np.random.rand()
               #print(w1) check which vectors are assigned randomly
                     try:
                     	voc[w2] = model.wv[w2]
                     except KeyError:
                     	voc[w2] = np.random.rand()
              #print(w2) check which vectors are assigned randomly
          
                     cos = 1 - spatial.distance.cosine(voc.get(w1),voc.get(w2))
                     system.append(cos)
                     gold.append(score)
  
     sim.close()
     return spearmanr(system, gold).correlation