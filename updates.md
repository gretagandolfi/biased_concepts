31.01.2020

__Broad topic__:  definition of biases expressed in language.  
Two main perspectives:

• philosophical:  concepts are characterised by properties.  Properties can benecessary (definitional) or additional.  A biased concept differs from a neutral one because of the different configuration of non-necessary properties. Let’s explore how these properties change.

• distributional:  biased concepts can be identified by their geometrical representation in the semantic space. We can look for a geometrical/operative definition that all (or the majority) of biased concepts can share.

__Proposal__:  take  two  polarised  communities  from  Reddit,  build  two  semantic spaces and compare them, focusing on some target concepts.  It can be hard to compare concepts coming from different semantic spaces since all concepts are connected and perturbations of a concept would result in perturbations of the semantic space as a whole.  An idea could be to use rotation/scaling at a global or at a local level in both the semantic spaces (and the code Aurelie provided) to check how different they are whether it makes sense to compare them.  If the experiment fails, we can analyse the reasons for this failure.

__! Idea__:  use  also  the  information  you  can  extract  about  speakers  since  language is strongly influenced by the identity of who produces it (Emily Bender workshop).

_To do_
•define some target concepts (e.g.  broad:  race, gender; narrow:  science in flat earth and round earth communities, etc.  )
•gather data
•try the code


_To read_
•Pia Sommerauer Master Thesis:  Conceptual Change and Distributional Semantic Models:  an Exploratory Study on Pitfalls and Possibilities.
•Literature on Bias, Distributional Semantics, Argumentation (2nd Workshop on Argumentation Mining, 2015), Meaning shift.


05.02.2020

Sometimes  data  from  a  particular  subreddit  (a  group  of  discussion)  is  not enough.  We decided to expand it, collecting all the data (max 1000 submissions -  posts  -  due  to  API  limitations  each)  from  the  moderators  and  the  related groups.  Now we are focusing on democrats vs republicans (very general,  can impact on the network of concepts as a whole).  Other possible topics can be:
•creationism vs evolutionism (r/Creation vs r/evolution)
•pro and anti-capital punishment (r/abolish vs ?)
•pro-life/pro-choice (r/prolife vs r/prochoice)
•opposite attitude towards a specific person (?)
•vegan and antivegan people (r/vegan vs r/AntiVegan)

We expect more localised perturbations in the latter case, for example.

_To do_
•gather data from democrats and republicans
•try fasttext on it
•make a repository to share + look at the code to compare the semantic spaces.

13.02.2020

I built two semantic spaces (with fasttext algorithm), one based on democratic data, the other on republican one.  As a test, I checked for the correlation with the similarity scores from MEN dataset.  The spearman correlation is very low
(0.2). We  decided  to  perform  a  parameter  tuning  process  (Bayesian  optimization), controlling for the hyperparameters of (1) the democrats model, (2) the republicans model, (3) the concatenated model (built starting from both the corpora).

__NULL  HYPOTHESIS__:  there  is  no  (statistically  significant)  difference  between the optimal parameters for the three model (data is consistent).

_To do_
•Bayesian optimization

20.02.2020

_To do_
•Control for the variations in and across the models.
•Define clear hypothesis.
•Fix the optimization issues.

_To read_
•Conceptual Change and Distributional Semantic Models:  an Exploratory Study on Pitfalls and Possibilities
•Evaluating the consistency of word embeddings from small data

_From the readings_:
An informal hypothesis can be:the semantic spaces modelling two different communities  should share  some  properties and,  at  the  same  time,  they should differ in some ways. I  should  find  a  method  to  be  sure  that  I  will  be  focusing  on  the real  differences in  the  spaces  and  not  the  ones  given  by random  factors impacting the act of modelling. I need to find a way to grasp and isolate the real shift of meaning.  Some factors that can have an impact on the research (possibly misleading results):
• frequency effect;
• initialisation of the model and order of data given to it;
• size of the dataset
To  check  if  they  differ,  I  should  operationalise  and quantify  the  expected difference (e.g.  through the rotation and scaling operations of (a) some  portions of the space or (b) of some target concepts).

If we choose (b),  we can assume that the study would be similar to the ones about  diachronic  changes  in  the  meaning  of  words. To  give  a  solid  methodological structure to the experiment I can:  
1.  define the process of target word selection using literature from social science, communication science, sociolinguistic or social psychology; 
2. try to differentiate between core concepts, relatedconcepts and subconcepts (related to the target words); 
3.  define control words.

I  can  select  some  target  concepts  and  look  for  their  variance  in  different corpora, compared to the (expected) lack of variance of control words.  To gain reliable results, I should compare the output of different models and check whether the expected movements/transformations of target concepts (concepts to be defined and movements to be hypothesised) are there, whether they come as we expect in all the models and so on. I should also check for the list of nearest neighbours of some target words in all the models and control for the ranking of some particular neighbours (to be defined).

To  check  for  the  goodness  of  the  models,  before  any  check  on  the  semantic changes, I can try to compute the consistency of the dataset (which is small), using aadditive model.

01.03.2020

The best thing to do is to create a strict plan (methodologically speaking).  I can start by the related work and then, I will write down my plan. Hints:

• use and additive model to check for the consistency of the space.  It would be  possible  to  run  different  experiment  and  check  for  the  target  words, with different training set.

• the results should be stable.

06.03.2020

To communicate, we should share some (but not all) the beliefs we have about concepts.  A semantic space is based on the use we do of words, and, assuming that its usage is a representation of meaning, it makes sense to expect that some words’ representation should be stable across spaces and some other should not. For example, democrats and republicans will agree on the meaning of the word ’cat’ but could have a different idea of the meaning of ’immigrant’. Here  we  have  the  first  problem:  is  it  true  that  people  with  different  (political) perspectives would not share any feature of the meaning of immigrant?  It is  more  plausible  that  they  agree  on  some  (crucial)  features  and  don’t  agree on other, non-necessary features.  
Indeed, they need to share some features to communicate.  Language  can  be  seen  as  a  combination  of  two  quasi-opposite
forces:  the freedom to be creative and the necessity to understand and be understood by the others. Different perspectives concerning the meaning of each word are allowed by the freedom of being creative in language, still being bound to the necessity of communication.  Aurelie showed how scaling,  rotation and translation (at a local or global level) can model this double-faced force in the language,  perturbating  parts  of  the  space  while  preserving  original  distances and alignment.

__RESEARCH  QUESTIONS__:  
(1)  can  these  measures  be  used  to  account  for the difference in polarised perspective about target concepts/target areas in the space?  
(2) Can they be used to normalise concepts that depart from their neutral form?

__EXPERIMENT__:  Compare  semantic  spaces  that  model  different  communities (e.g.  dem, rep, neutral). 
First, select concepts or topics that are not expected to be different.  It can be done automatically (clustering) or manually (theory-driven).  Or both.

Second, check if there is a shift in their meaning.  At a trivial level.

Third,  control  for  their  difference.   Do  they  really  differ  or  do  they  just  look different?  Control for the impact of random factors, such as the size of the corpus, the order of data presentation, the model used and so on.

Fourth,  apply  the  vectorial  operations  to  quantify  the  difference  between  the neutral and the biased corpora.  Is there a significant difference between target and neutral concepts?

Fifth,  are  the  results  domain-dependent?   Check  for  other  hubs  of  discussion (...).  Are the results consistent?

__Some problems__:
• Size and quality of the corpora.  Mine are really small.  Possible solutions:
(1)  train  the  model  on  the  neutral  corpus  (or  take  pre-trained  embed-
dings), evaluate, keep training it on dem/rep, evaluate;
(2) additive model
(3) Nonce2Vec (?)
(4) if the previous ones don’t work, ask for the corpus used in Azarbonyad, Hosein   Dehghani,  Mostafa   Beelen,  Kaspar   Arkut,  Alexandra   Marx, Maarten   Kamps,  Jaap.   (2017).   Words  are  Malleable:  Computing  Semantic Shifts in Political and Media Discourse.
• Method  to  select  concepts,  automatic  (clustering:   following  the  theory of  prototypes  which  relies  on  the  fact  that  words  that  are  closer  to  the cluster centroid are less likely to change (in time)), manual (theory driven analysis,  more  stable  but  also  longer  +  needs  for  expert)  or  manual  + automatic;
• How to define the movement that I’m expecting.  It depends on the way I used to select the concepts.
• Errors can be due to problems at every stage.  It would be also interesting to understand and analyse why some errors come up (or why some models seem to provide evidence for a phenomenon and some others don’t).
• Risk of circularity.

_To do_
• state the possible problems and solutions in a more concrete way.
• prioritise some problems with respect to others.
• check  practically  if  it  is  possible  to  proceed  (at  list  at  the  level  of  the
dataset (first point in the list of problems).
• read broad papers, from which I can take more inspirations

16.03.2020

Re-formulation of already discussed problems: 

- __data size__: my corpora are small and the models reflect this fact. I thought about some solutions: 
	* increase data size (I identified other Reddit  sub-communities that can be used to provide data produced by democrats and republicans. They are listed in Soliman, Ahmed & Hafer, Jan & Lemmerich, Florian. 	(2019). A Characterization of Political Communities on Reddit. 259-263. 10.1145/3342220.3343662. The paper is more about the network structure rather than the meaning of what the users wrote but they did an 	interesting preliminary work to identify political hubs on Reddit; 
	* use a __pretrained model and keep training on both corpora__. So to have three models (neutral model built upon Wikipedia vectors, wiki + dem, wiki + rep) (+);
	* use more fine graded __methods to deal with small data__: 
	
		> Nonce2Vec 
		
		> Additive model
		
		> Concatenated model (with marked target concepts). 

- __concept selection__: how to select and make a hypothesis on the difference expected. 
	* _manual selection_: top-down. In this paper, Barberá, P., Jost, J. T., Nagler, J., Tucker, J. A., & Bonneau, R. (2015). Tweeting From Left to Right: Is Online Political Communication More Than an Echo Chamber? Psychological Science, 26(10), 1531–1542. https://doi.org/10.1177/0956797615594620, they developed a measure to provide the amount of polarisation per topic in Twitter discussion. In the additional material, they listed some concepts, related to a few topics, which have been controversial in twitter political discussions paired with more neutral concepts. 
	* _automatic selection_: clustering and demonstrating whether the rule of prototypicality (the vectors that are closer to the centroid are less likely to change in time), proved to work in diachronic shift, work also in this context or not. 
This method can be applied also to other hubs of discussion (as we thought: pro-life, pro-choice; creationism vs evolutionism), while the other method requires time/effort/expert consultation on every new topic. 

- __choice of baseline method to be compared__. There are several methods, all listed in the survey Survey of Computational Approaches to Lexical Semantic Change Nina Tahmasebi, Lars Borin, Adam (2018) to compute the diachronic semantic shift that can be applied in this context.

Meanwhile, I started working on this step (+). I used the pretrained vectors (from here https://fasttext.cc/docs/en/pretrained-vectors.html). The initial model correlates with the similarity judgements in the MEN dataset (0.76), while the new models, trained also on my corpora reach 0.68. I haven’t worked on parameters yet. 
Now I’m searching a way to save the models in a format compatible with the code that Aurelie provided me with (speakers in a vat). 

_To do_: 

• increase corpora (new subreddit), to decrease the chance of noise; +

• re-train models controlling for the learning rate; 

• consider the mixed corpora strategy (contact Jelke Bloem in case); 

• save the models in the proper format; +

• look at the thesis of the previous master students in Trento; +

• start writing 'related work' section. +



23.03.2020

a) I started writing the related work section, that, by now has this (draft) structure: 

1. What is Distributional Semantics?

2. Biases in DS. 

 	2.1 What is bias? Literature from cognitive science, sociology and so on + relation between bias and stereotypes. 
 
 	2.2 Work on bias in distributional semantics: descriptive works and debasing methods
 
3. Meaning shift as a method to identify different perspectives —> stereotypical views

4. Measuring perturbations methods


b) I expanded the corpora. New correlation scores: 
•  pre-trained model gives always 0.76 (old: 0.76)
•  pre-trained + dem: 0.71 (old, smaller: 0.68)
 •  pre-trained + rep: 0.69 (old, smaller: 0.68)


_To do_: 

* optimisation particularly focused on the learning rate; 

* random perturbation of the pre-trained model (to be used as the baseline comparison)

* keep writing +

* check the argumentation mining literature +

* consider the mixed corpora strategy (contact Jelke Bloem in case); 

29.03.2020

I kept writing. I'm planning to be ready to propose something concrete to you for the end of next week.
I checked the perturbation strategies suggested by Aurelie (Gaussian noise. I'm trying to understand how to implement it on my models). 

Moreover, I had a new idea: I read this paper: Sudeep Bhatia, The semantic representation of prejudice and stereotypes, Cognition, Volume 164, 2017 and I noticed how they showed that the amount of stereotypes revealed by LSA models strongly relies on their dimensionality (less dimension, more stereotype). It could be nice to compare the same model, applying post-processing dimensionality reduction and check how our analysis of biases change. This can be a way to: 
* check whether the dimensionality factor impacts on word-embeddings
* control for random factors and avoid pitfalls

In this other paper: Word Embedding Perturbation for Sentence Classification (2018), Dongxu Zhang and Zhichao Yang show how to apply dimensionality reduction (with 3 different methods) on pre-trained models (including one created with fasttext on wiki data - our case) without losing accuracy. 

02.04.2020

_To do_:

* apply the gaussian perturbation on the whole control corpus (summing the vectors, then I should be do it locally); 

* take 10 iteration with different learning rates 

* to select the target concepts: TFIDF + target terms

* On the measures of perturbation: 
	- RSA gives a general measure of how much a concept changed;
	- __SimLex__ is better for evaluation (MEN has more concrete objects);
	- isolation is not so meaningful in this context;
	- __rotation__ is the relevant concept. 
