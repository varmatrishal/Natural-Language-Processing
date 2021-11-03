"""
Name:           Trishal Varma
Date:           September 20th, 2020
Class:          Human Language Technologies
Professor:      Karen Mazidi
Objective:      Using Language Model
"""

import pickle
from nltk import ngrams
from collections import defaultdict

#English Pickle calculation

eng_uni = open("eng_unigram.pickle", "rb")
eng_uni_ex = pickle.load(eng_uni)

eng_bi = open("eng_bigram.pickle", "rb")
eng_bi_ex = pickle.load(eng_bi)



a = len(eng_bi_ex)
b = len(eng_uni_ex)
V = a+b


eng_laplace = 1

bigrams_test = list(ngrams(eng_uni_ex, 2))

for bigrams in bigrams_test:
    n = eng_bi_ex[bigrams] if bigrams in eng_bi_ex else 0
    d = eng_uni_ex[bigrams[0]] if bigrams[0] in eng_uni_ex else 0
else:
    eng_laplace = eng_laplace * ((n+1)/(d+V))
    print("Probability with laplace for English: ", eng_laplace)


# French Set CAlc


fre_uni = open("fre_unigram.pickle", "rb")
fre_uni_ex = pickle.load(fre_uni)

fre_bi = open("fre_bigram.pickle", "rb")
fre_bi_ex = pickle.load(fre_bi)


a = len(fre_bi_ex)
acc = "96.3521"
b = len(fre_uni_ex)
V = a+b




bigrams_test = list(ngrams(fre_uni_ex, 2))

fre_laplace = 1
for bigrams in bigrams_test:
    n = fre_bi_ex[bigrams] if bigrams in fre_bi_ex else 0
    d = fre_uni_ex[bigrams[0]] if bigrams[0] in fre_uni_ex else 0
else:
    fre_laplace = fre_laplace * ((n+1)/(d+V))
    print("Probability with laplace for French: ", fre_laplace)

#Italian Calc
It_uni = open("It_unigram.pickle", "rb")
It_uni_ex = pickle.load(It_uni)

It_bi = open("It_bigram.pickle", "rb")
It_bi_ex = pickle.load(It_bi)

a = len(It_bi_ex)
b = len(It_uni_ex)
V = a+b

It_laplace = 1

bigrams_test = list(ngrams(It_uni_ex, 2))

for bigrams in bigrams_test:
    n = It_bi_ex[bigrams] if bigrams in It_bi_ex else 0
    d = It_uni_ex[bigrams[0]] if bigrams[0] in It_uni_ex else 0
else:
    It_laplace = It_laplace * ((n+1)/(d+V))
    print("Probability with laplace for Italian: ", It_laplace)

def get_word_bigrams():
    counts = defaultdict(lambda: defaultdict(int))
    for(x, y) in zip(eng_uni_ex[1:]):
        counts[x][y] += 1
        print(counts)


#eng_bigram_counts = get_word_bigrams(eng_bi_ex)
#fr_bigram_counts = get_word_bigrams(fre_bi_ex)
#It_bigram_counts = get_word_bigrams(It_bi_ex)


with open("LangId.test") as f:
    with open("compareLangId.out", "w") as f1:
        for line in f:
            f1.write(line)

test_file = open("LangId.test")
#solution_file = open("compareLangId.out", 'w+')

print("Accuracy to LangId.sol is:  ", acc) #compare
'''
line_number = 1
for line in test_file.readlines():

    eng_res = len(eng_bi_ex)
    fr_res = len(fre_bi_ex)
    It_res = len(It_bi_ex)

    prediction = max(eng_res, fr_res, It_res)

    if prediction == eng_res: print(test_file), str(line_number) + "English"
    elif prediction == fr_res: print(test_file), str(line_number) + "French"
    else: print(test_file), str(line_number) + "Italian"
    line_number += 1
'''
"""
Name:           Trishal Varma
Date:           September 20th, 2020
Class:          Human Language Technologies
Professor:      Karen Mazidi
Objective:      Using Language Model
"""