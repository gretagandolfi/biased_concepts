import re
import pickle
import gensim
import numpy as np
import pandas as pd
import nltk
import pickle
import random
from gensim.models.fasttext import FastText
from scipy.stats import spearmanr
from scipy import spatial
from bayes_opt.observer import JSONLogger
from bayes_opt.event import Events
from bayes_opt import BayesianOptimization 


model_path = '/Volumes/greta/models/model1.bin' 
model1 = FastText.load_fasttext_format(model_path)
model1.alpha
#0.025

corpus_path = '/Users/gretagandolfi/Dropbox/thesis/progetto/fasttext/rep_aggiornato.pkl'
corpus = pickle.load(open(corpus_path, 'rb'))


def correlates_SIM(start_alpha):
	model = model1 
	model.train(sentences=corpus, total_examples=len(corpus), epochs=model1.epochs, start_alpha=float(start_alpha))
	
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


pbounds = {'start_alpha': (0.01,0.1)}
optimizer = BayesianOptimization(f=correlates_SIM, pbounds=pbounds)

logger = JSONLogger(path="/Users/gretagandolfi/Desktop/logs_rep.json")
optimizer.subscribe(Events.OPTMIZATION_STEP, logger)
print(optimizer.maximize(init_points=2, n_iter=10))
