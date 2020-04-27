# packages
import re
import numpy
import pickle
import gensim
import math
import correlations
from gensim.models.fasttext import FastText
from scipy.stats import spearmanr
from scipy import spatial
import itertools

#pretrained model (default parameters, 300 dimensions)
model_path = '/Volumes/greta/models/model1.bin' 
model1 = FastText.load_fasttext_format(model_path)

model1.wv.vectors = control

def normalise(x):
	return (x-min(x))/(max(x)-min(x))
def divide_chunks(l, n): 
     for i in range(0, len(l), n):  
         yield l[i:i + n]

#GLOBAL PERTURBATION
def create_perturbation(x):
	pert_space = []
	for i in model1.wv.vectors:
		noise = []
		for j in normalise(i).tolist():
			noise.append(math.pow(j,x))
		pert_space.append(numpy.array(noise))
	pert = numpy.stack(pert_space)
	control = model1.wv.vectors
	model1.wv.vectors = pert 
	MEN = correlations.correlates(model1)
	SIM = correlations.correlates_SIM(model1)
	return print('M:', MEN, '/n', 'S:', SIM)

#LOCAL PERTURBATION
#create vocabulary
vocab = []
for k,v in model1.wv.vocab.items():
     vocab.append(k)
 

def create_perturbation_local(y,bin):
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
		noise = []
		for j in normalise(i).tolist():
			noise.append(math.pow(j,y))
		pert_space.append(numpy.array(noise))
	pert0 = list(itertools.chain(vec_before,pert_space,vec_after))
	pert = numpy.stack(pert0)
	model1.wv.vectors = pert 
	MEN = correlations.correlates(model1)
	SIM = correlations.correlates_SIM(model1)
	return print('M:', MEN, '/n', 'S:', SIM)
	

start = 0.1
stop = 2.0
step = 0.1
float_range_array = numpy.arange(start, stop, step)
for i in float_range_array:
	model1.wv.vectors = control
	print(create_perturbation(i))


	