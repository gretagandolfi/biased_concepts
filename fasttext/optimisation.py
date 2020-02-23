
import re
import pickle
import random
import numpy as np
import pandas as pd
from gensim.models.fasttext import FastText
from bayes_opt import BayesianOptimization 
from bayes_opt.observer import JSONLogger
from bayes_opt.event import Events
from scipy import spatial
from scipy.stats import spearmanr


corpus = pickle.load(open('word_tokenized_corpus_dem.pkl', 'rb')) 


def correlation_function(embedding_size, window_size, min_word, down_sampling, negative):
    
    model = FastText(corpus,  
                     size=int(embedding_size), 
                      window=int(window_size),
                      min_count=int(min_word),
                      sample=int(down_sampling), negative=int(negative),
                      sg=int(1))

    sim = open('/Users/gretagandolfi/Desktop/thesis/progetto/corpus/MEN/MEN_dataset_natural_form_full.txt', 'r')
    system = []
    gold = []
    voc = {}
    
    for l in sim:
        fields = l.rstrip('\n').split()
        w1 = fields[0].replace("-n",".n")    
        w2 = fields[1].replace("-n",".n")
        score = float(fields[2])
        try:
            voc[w1] = model.wv[w1]
        except KeyError:
            voc[w1] = np.random.rand(int(embedding_size))
            #print(w1) check which vectors are assigned randomly
        try:
            voc[w2] = model.wv[w2]
        except KeyError:
            voc[w2] = np.random.rand(int(embedding_size))
            #print(w2) check which vectors are assigned randomly
       
        cos = 1 - spatial.distance.cosine(voc.get(w1),voc.get(w2))
        system.append(cos)
        gold.append(score)
        
    sim.close() 
    print(len(voc))
            
    return spearmanr(system, gold).correlation

correlation_function(300,20,23,0,5)

# check whether the vocabulary contains all the words provided by MEN dataset: 
#compare the printed number of the previous function and the following one
sim = open('/Users/gretagandolfi/Desktop/thesis/progetto/corpus/MEN/MEN_dataset_natural_form_full.txt', 'r').read() 
sim = sim.split()
sim = [i for i in sim if i.isalpha()]
len(set(sim))

pbounds = {'embedding_size': (5,300), 
           'window_size': (3,20), 
           'min_word': (20,200), 
           'down_sampling': (1e-5,0), 
           'negative': (5,20)}

optimizer = BayesianOptimization(f=correlation_function, pbounds=pbounds)

logger = JSONLogger(path="./logs.json")

optimizer.subscribe(Events.OPTMIZATION_STEP, logger)

optimizer.maximize(init_points=2, n_iter=100)
