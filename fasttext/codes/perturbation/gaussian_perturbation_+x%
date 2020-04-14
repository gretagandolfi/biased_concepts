# packages
import re
import pickle
import gensim
from gensim.models.fasttext import FastText
from scipy.stats import spearmanr
from scipy import spatial
import numpy
import correlations

#pretrained model (default parameters, 300 dimensions)
model_path = '/Volumes/greta/models/model1.bin' 
model1 = FastText.load_fasttext_format(model_path)


#compute percentage
def percentage(part, whole):
  return float(part)*float(whole)/100

#vectors of the control space
control = model1.wv.vectors 

def create_perturbation_G(x):
	pert_space = []
	for i in model1.wv.vectors:
		noise=[]
		mu = percentage(x,numpy.mean(i))
	sigma = percentage(x,numpy.std(i))
	noise = numpy.random.normal(mu, sigma, 300)
	pert_i = i + noise
	pert_space.append(pert_i)
	pert = numpy.array(pert_space)
	pert = model1.wv.vectors - pert
	model1.wv.vectors = pert 
	MEN = correlations.correlates(model1)
	SIM = correlations.correlates_SIM(model1)
	return print('M:', MEN, 'S:', SIM)

for i in range(10,100,10):
	model1.wv.vectors = control
	print(create_perturbation_G(i))


