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

#pretrained model (default parameters, 300 dimensions)
model_path = '/Volumes/greta/models/model1.bin' 
model1 = FastText.load_fasttext_format(model_path)

model1.wv.vectors = control

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

start = 0.1
stop = 0.9
step = 0.1
float_range_array = numpy.arange(start, stop, step)

for i in float_range_array:
	model1.wv.vectors = control
	print(create_perturbation(i))
