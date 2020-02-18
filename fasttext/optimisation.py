from scipy.stats import spearmanr
from scipy import spatial
import pickle
from gensim.models.fasttext import FastText

sim = open('MEN_dataset_natural_form_full.txt', 'r')
word_tokenized_corpus = pickle.load(open('word_tokenized_corpus.pkl', 'rb'))

def function(embedding_size, window_size, #min_word, 
             down_sampling, negative):
    
    model = FastText(word_tokenized_corpus,  size=embedding_size,
                      window=window_size,
                      #min_count=min_word,
                      sample=down_sampling, negative=negative,
                      sg=1)

    system = []
    gold = []
    for l in sim:
        fields = l.rstrip('\n').split()
        w1 = fields[0].replace("-n",".n")    
        w2 = fields[1].replace("-n",".n")
        score = float(fields[2])
        if w1 in model.wv.vocab and w2 in model.wv.vocab:
            cos = 1 - model.wv.similarity(w1,w2)
            system.append(cos)
            gold.append(score)      
            
    return spearmanr(system, gold).correlation
    
    
print(function(300,20,0,5))

from bayes_opt import BayesianOptimization 
pbounds = {'embedding_size': (5,300), 'window_size': (3,20), #'min_word': (20,200), 
           'down_sampling': (0, 1e-5), 'negative': (5,20)}
optimizer = BayesianOptimization(f=function, pbounds=pbounds)


optimizer.maximize(
    init_points=2,
    n_iter=100)
