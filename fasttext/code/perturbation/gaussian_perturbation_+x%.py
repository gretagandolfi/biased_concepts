# packages
import re
import pickle
import gensim
from gensim.models.fasttext import FastText
from scipy.stats import spearmanr
from scipy import spatial
import numpy
import correlations
import itertools

#pretrained model (default parameters, 300 dimensions)
model_path = '/Volumes/greta/models/model1.bin' 
model1 = FastText.load_fasttext_format(model_path)
 


#compute percentage
def percentage(part, whole):
  return float(part)*float(whole)/100

#vectors of the control space
control = model1.wv.vectors 

def divide_chunks(l, n): 
     for i in range(0, len(l), n):  
         yield l[i:i + n]

#create vocabulary
vocab = []
for k,v in model1.wv.vocab.items():
     vocab.append(k)

def create_perturbation_G(x):
	pert_space = []
	for i in model1.wv.vectors:
		noise=[]
		mu = percentage(x,numpy.mean(i))
		sigma = percentage(x,numpy.std(i))
		noise = numpy.random.normal(mu, sigma, 300)
		pert_i = i - noise
		pert_space.append(pert_i)
	
	pert = numpy.array(pert_space)
	pert = model1.wv.vectors + pert
	model1.wv.vectors = pert 
	
	MEN = correlations.correlates(model1)
	SIM = correlations.correlates_SIM(model1)
	return print('M:', MEN, 'S:', SIM)

for i in range(10,100,10):
	model1.wv.vectors = control
	print(create_perturbation_G(i))


#whole function
def create_perturbation_local_G_add(y,bin):
     dec = len(vocab)/1000
     x = list(divide_chunks(vocab, int(dec)))
     vec_x = [model1.wv[i] for i in x[bin]]
     vec_before = []
     for i in x[:bin]:
             for j in i:
                     vec_before.append(model1.wv[j])
     vec_after = []
     for i in x[bin+1:]:
             for j in i:
                     vec_after.append(model1.wv[j])
     pert_space = []
     for i in vec_x:
             noise=[]
             mu = percentage(y,numpy.mean(i))
             sigma = percentage(y,numpy.std(i))
             noise = numpy.random.normal(mu, sigma, 300)
             pert_i = i + noise
             pert_space.append(pert_i)
     
     pert0 = list(itertools.chain(vec_before,pert_space,vec_after))
     pert = numpy.stack(pert0)
     pert = model1.wv.vectors + pert
     model1.wv.vectors = pert 
     MEN = correlations.correlates(model1)
     SIM = correlations.correlates_SIM(model1)
     return print('M:', MEN, '/n', 'S:', SIM)

def create_perturbation_local_G_min(y,bin):
	dec = len(vocab)/1000
	x = list(divide_chunks(vocab, int(dec)))
	vec_x = [model1.wv[i] for i in x[bin]]
	
	vec_before = []
	for i in x[:bin]:
		for j in i:
			vec_before.append(model1.wv[j])
	
	vec_after = []
	for i in x[bin+1:]:
		for j in i:
			vec_after.append(model1.wv[j])
	
	pert_space = []
	for i in vec_x:
		noise=[]
		mu = percentage(y,numpy.mean(i))
		sigma = percentage(y,numpy.std(i))
		noise = numpy.random.normal(mu, sigma, 300)
		pert_i = i - noise
		pert_space.append(pert_i)
	
	pert0 = list(itertools.chain(vec_before,pert_space,vec_after))
	pert = numpy.stack(pert0)
	pertu = model1.wv.vectors + pert
	model1.wv.vectors = pertu 
	MEN = correlations.correlates(model1)
	SIM = correlations.correlates_SIM(model1)
	return print('M:', MEN, '/n', 'S:', SIM)


