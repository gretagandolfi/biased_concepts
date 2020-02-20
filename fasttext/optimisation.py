from scipy.stats import spearmanr
from scipy import spatial
import pickle
from gensim.models.fasttext import FastText


word_tokenized_corpus = pickle.load(open('word_tokenized_corpus.pkl', 'rb'))

def correlation_function(embedding_size, window_size, min_word, 
             down_sampling, negative):
    
    model = FastText(word_tokenized_corpus,  size=int(embedding_size),
                      window=int(window_size),
                      min_count=int(min_word),
                      sample=int(down_sampling), negative=int(negative),
                      sg=1)
    
    sim = open('MEN_dataset_natural_form_full.txt', 'r')
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
    
    sim.close()
    return spearmanr(system, gold).correlation
    
    
print(correlation_function(300,20,23,0,5))

from bayes_opt import BayesianOptimization 
pbounds = {'embedding_size': (5,300), 'window_size': (3,20), 'min_word': (20,200), 
           'down_sampling': (0, 1e-5), 'negative': (5,20)}
optimizer = BayesianOptimization(f=correlation_function, pbounds=pbounds)


optimizer.maximize(
    init_points=2,
    n_iter=100)
