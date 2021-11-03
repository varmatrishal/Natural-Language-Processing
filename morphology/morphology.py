"""
Name:           Trishal Varma
Date:           September 12th, 2020
Class:          Human Language Technologies
Professor:      Karen Mazidi
Objective:      Using Morphology
"""

import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy

# Reading moby dick from the text file.
ps = PorterStemmer()
f = open("moby_dick.txt")
text = f.read()
f.close()

# Pre Processing
text = text.lower()
text = text.replace('--', '')
text = re.sub("\d+", "", text)
text_copy = text
text = re.sub(r'''[,.@#?!&$'"()]+''', "", text)

#tokenize
tokens = nltk.word_tokenize(text)
print("The number of tokens:", len(tokens))
# Unique tokens
unique_set = set(tokens)
print("The number of unique tokens: ", len(unique_set))
# list of important words
important_words = [word for word in unique_set if not word in stopwords.words()]
print("The number of important words: ", len(important_words))

important_stemmed_word = []
for word in important_words:
    important_stemmed_word.append((word, ps.stem(word)))
print("Tuples list of the word and stemmed word: ", important_stemmed_word)


# Dict. of key is stem value of stem listed.
stem_dict = {}
for word in important_stemmed_word:
    if word[1] in stem_dict:
        if word[0] not in stem_dict[word[1]]:
            stem_dict[word[1]].append(str(word[0]))
    else:
        stem_dict[word[1]] = [word[0]]
print("Length of the stem words dict: ", len(stem_dict))
# lenght of the dictionary

count = 0
print("The longest list in from stem words: ")
for k in sorted(stem_dict, key=lambda k: len(stem_dict[k]), reverse=True):
    if count != 25:
        print(k, "\t: \t", stem_dict[k])
        count += 1


# Levenshtein Distance Step 10
def iterative_levenshtein(s,t):

    rows = len(s) + 1
    cols = len(t) + 1
    dist = [[0 for x in range(cols)] for x in range(rows)]
    for i in range(1, rows):
        dist[i][0] = i

    for i in range(1, cols):
        dist[0][i] = i

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row - 1] == t[col - 1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row - 1][col] + 1,
                                 dist[row][col - 1] + 1,
                                 dist[row - 1][col - 1] + cost)

    for r in range(rows):
        print(dist[r])

    return dist[row][col]

print(iterative_levenshtein("continue", "continu"))

# step 11 POS tagging
tagged = nltk.pos_tag(text_copy.split())

# creating dictionary
pos_count = {}
for word in tagged:
    if word[1] in pos_count:
        pos_count[word[1]] += 1
    else:
        pos_count[word[1]] = 1
print("The dictionary POS count: \n", pos_count)

# rnd
"""
Name:           Trishal Varma
Date:           September 12th, 2020
Class:          Human Language Technologies
Professor:      Karen Mazidi
Objective:      Using Morphology
"""