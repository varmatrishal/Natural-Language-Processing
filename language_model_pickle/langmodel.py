"""
Name:           Trishal Varma
Date:           September 20th, 2020
Class:          Human Language Technologies
Professor:      Karen Mazidi
Objective:      Using Language Model
"""

import nltk
import nltk.corpus
import pickle
from nltk.util import ngrams
import fileinput

# English
file = open(input("Enter English File:  'LangId.train: ")).read()

for line in fileinput.FileInput("LangId.train.English", inplace=1):
    if line.rstrip():
        print(line)


eng_unigram = nltk.word_tokenize(file)

eng_bigrams = [(eng_unigram[k], eng_unigram[k+1]) for k in range (len(eng_unigram)-1)]

eng_unigram_dict = {t:eng_unigram.count(t) for t in set(eng_unigram)}

#PICKLE
with open("eng_unigram.pickle", "wb") as handle:
    pickle.dump(eng_unigram_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open("eng_unigram.pickle", "rb") as handle:
    b = pickle.load(handle)

eng_bigram_dict = {b:eng_bigrams.count(b) for b in set(eng_bigrams)}

#PICKLE
with open("eng_bigram.pickle", "wb") as handle:
    pickle.dump(eng_bigram_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open("eng_bigram.pickle", "rb") as handle:
    b = pickle.load(handle)




# French
file = open(input("Enter French File:  'LangId.train: ")).read()

for line in fileinput.FileInput("LangId.train.French", inplace=1):
    if line.rstrip():
        print(line)


fre_unigrams = nltk.word_tokenize(file)


fre_bigrams = [(fre_unigrams[k], fre_unigrams[k+1]) for k in range (len(fre_unigrams)-1)]

fre_unigram_dict = {t:fre_unigrams.count(t) for t in set(fre_unigrams)}
#PICKLE
with open("fre_unigram.pickle", "wb") as handle:
    pickle.dump(fre_unigram_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open("fre_unigram.pickle", "rb") as handle:
    b = pickle.load(handle)

fre_bigram_dict = {b:fre_bigrams.count(b) for b in set(fre_bigrams)}
#PICKLE
with open("fre_bigram.pickle", "wb") as handle:
    pickle.dump(fre_bigram_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open("fre_bigram.pickle", "rb") as handle:
    b = pickle.load(handle)


#Italian
file = open(input("Enter Italian File:  'LangId.train: ")).read()

for line in fileinput.FileInput("LangId.train.Italian", inplace=1):
    if line.rstrip():
        print(line)


It_unigrams = nltk.word_tokenize(file)


It_bigrams = [(It_unigrams[k], It_unigrams[k+1]) for k in range (len(It_unigrams)-1)]

It_unigram_dict = {t:It_unigrams.count(t) for t in set(It_unigrams)}
#PICKLE
with open("It_unigram.pickle", "wb") as handle:
    pickle.dump(It_unigram_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open("It_unigram.pickle", "rb") as handle:
    b = pickle.load(handle)

It_bigram_dict = {b:It_bigrams.count(b) for b in set(It_bigrams)}
#PICKLE
with open("It_bigram.pickle", "wb") as handle:
    pickle.dump(It_bigram_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open("It_bigram.pickle", "rb") as handle:
    b = pickle.load(handle)


"""
Name:           Trishal Varma
Date:           September 20th, 2020
Class:          Human Language Technologies
Professor:      Karen Mazidi
Objective:      Using Language Model
"""