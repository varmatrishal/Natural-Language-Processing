"""
Name:           Trishal Varma

Human Language Technologies

Objective:     Creating a Chatbot with webscraped document to give informational responses to the user
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# this is ashley and I am to provide you with answers for the chatbot, any chatbot

# import necessary libraries

import string  # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings

warnings.filterwarnings('ignore')


'''
The Gensim LDA models will give us an idea of topics that we can ask Ashley (Chatbot) about" 
'''

num_docs = 1
docs = []
with open('chatbot.txt', 'r') as f:
    doc_chat = f.read().lower()
    doc_chat = doc_chat.replace('\n',' ')
    docs.append(doc_chat)

for i in range(num_docs):
    print("What is a chatbot: \n",docs[i][:80]) # First line displayed from the chatbot.txt read.

from gensim import models, corpora
from nltk import word_tokenize
from nltk.corpus import stopwords

NUM_TOPICS = 5
# number of topics we are looking for in this document. This can be increased or decreased depending on the topics we
# have.

# Preprocessing the text form the chatbot.txt
def preprocess(docs, stopwords):
    processed_docs = []
    for doc in docs:
        tokens = [t for t in word_tokenize(doc.lower()) if t not in stopwords
                  and t.isalpha()]
        processed_docs.append(tokens)
    return processed_docs

# displaying the 6 stopwords from preprocessed text.
preprocessed_docs = preprocess(docs, stopwords.words('english'))
for i in range(num_docs):
    print(preprocessed_docs[i][:6])

# showing the use of words and the length of the dictionary.
dictionary = corpora.Dictionary(preprocessed_docs)
print('len of dictionary: ', len(dictionary))
corpus = [dictionary.doc2bow(tokens) for tokens in preprocessed_docs]
print(corpus[0][:5])
print(dictionary[4], dictionary[2], dictionary[1])

# Creating the LDA model
lda_model = models.LdaModel(corpus=corpus, num_topics=NUM_TOPICS, id2word=dictionary)
for i in range(NUM_TOPICS):
    top_words = [t[0] for t in lda_model.show_topic(i,10)]
    print("\nTopics", str(i), ':', top_words)

print("\nThe Gensim LDA model gives us idea of the Topics we could ask the Chatbot about "
      "ex: Messi, whisky, chatbot")



import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('popular', quiet=True)  # for downloading packages

# here we are making a unique user model for each of the people persons
myDict = {}
# keeps the i like statement for each user
userslikings = {}

# download these two they are absolutely necessary
nltk.download('punkt')
nltk.download('wordnet')

# were are reading the file that we are going to eventually use
with open('chatbot.txt', 'r', encoding='utf8', errors='ignore') as theFile:
    itIt = theFile.read().lower()

# here we would do the tokenation
# list of sentences
sentencesIt = nltk.sent_tokenize(itIt)


# this here function checks if there are any keys that already exist in the chatbot
def checkIt(dict, key):
    if key in dict.keys():
        return True
    else:
        return False

    # Preprocessing it


lemmer = WordNetLemmatizer()


def lemmmit(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


changePunct = dict((ord(punct), None) for punct in string.punctuation)


# normalizing it
def normalize(text):
    return lemmmit(nltk.word_tokenize(text.lower().translate(changePunct)))


# Keyword Matching
commongreetings = (
"salam", "hello", "nihow", "hi", "how are you", "greetings", "how\'s it going", "sup", "what's up", "hey",)


# this interacts with the saying hi of the user
def sayingHIIt(inputt):
    """If user's input is a greeting, return a greeting response"""
    for word in inputt.split():
        if word.lower() in commongreetings:
            return "hi dude"


# Generating response
def responseToUser(ourInput, name):
    introduce = ourInput
    botAnswer = ''
    if ("i'm" in ourInput or "i am" in ourInput or "my name is" in ourInput or "My name is" in ourInput):
        if "i am" in ourInput:
            ourInput = ourInput.replace("i am ", isname + " you are ")
        elif "i\'m" in ourInput:
            ourInput = ourInput.replace("i\'m ", isname + " you are ")
        else:
            ourInput = "you\'ve once before thought about " + ourInput
    if ourInput not in myDict[name]:
        myDict[name].append(ourInput)

    print(myDict[name])
    TfidfVec = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(myDict[name])

    # cosine similarity use to find commonality
    vals = cosine_similarity(tfidf[-1], tfidf)

    # this is index goes up to
    idx = vals.argsort()[0][-2]

    # this flattens the whole thing
    roundddd = vals.flatten()
    roundddd.sort()

    # this is the tfidf that gets used
    req_tfidf = roundddd[-2]

    # if the sentence said doesn't match anything
    if (req_tfidf == 0):
        botAnswer = botAnswer + "I didn\'t get what you just said"
        return botAnswer
    else:
        botAnswer = botAnswer + myDict[name][idx]
        return botAnswer


indicator = True
print(
    "Ashley: My name is Ashley. I will get to know you and answer your questions about any chatbots that you want. "
    "If you want to exit, type \"leaving the chatbot\"!")

# this is where the user talks to it
while (indicator == True):

    print("First tell me who am I speaking with?(only your name please)")
    isname = input()
    isname = isname.lower()

    # checking if user exists
    if not checkIt(myDict, isname):
        myDict[isname] = []
        myDict[isname] = myDict[isname] + (sentencesIt)

    # interact with user
    if (checkIt(userslikings, isname)):
        print(userslikings[isname][0])

    # learning things about the user
    print("Tell me something about yourself " + isname)
    print("feel free to tell me about your passions by saying \"I like\" before the statement you make")
    ourInput1 = input()
    ourInput1 = ourInput1.lower()

    # parsing user's input
    if ("i'm" in ourInput1 or "i am" in ourInput1 or "my name is" in ourInput1 or "My name is" in ourInput1
            or "i like" in ourInput1):
        if "i am" in ourInput1:
            ourInput1 = ourInput1.replace("i am ", isname + " you are ")
        elif "i\'m" in ourInput1:
            ourInput1 = ourInput1.replace("i\'m ", isname + " you are ")
        elif "i like" in ourInput1:
            ourInput1 = ourInput1.replace("i like ", isname + " you like ")
            if not checkIt(userslikings, isname):
                userslikings[isname] = []
                userslikings[isname].append(ourInput1)
            else:
                userslikings[isname].append(ourInput1)

        else:
            ourInput1 = "you are " + ourInput1

    print("I love " + isname + " as much as you - " + ourInput1 + "!")
    myDict[isname].append(ourInput1)

    print("what do you want to know " + isname)
    ourInput = input()
    ourInput = ourInput.lower()
    if (ourInput != 'leaving the chatbot'):
        if (ourInput == 'you are goat' or ourInput == 'I love you'):
            indicator = False
            print("Ashley: I love you too mate")
        else:
            if (sayingHIIt(ourInput) != None):
                print("Ashley: " + sayingHIIt(ourInput))
            else:
                print("Ashley: ", end="")
                print(responseToUser(ourInput, isname))

    else:
        indicator = False
        print("Ashley: I\'m leaving I hate you.")


    myDict[isname].append(ourInput1)

    print("Anything else you want to know " + isname+ "?")
    ourInput = input()
    ourInput = ourInput.lower()
    if (ourInput != 'leaving the chatbot'):
        if (ourInput == 'you are goat' or ourInput == 'I love you'):
            indicator = False
            print("Ashley: I love you too mate")
        else:
            if (sayingHIIt(ourInput) != None):
                print("Ashley: " + sayingHIIt(ourInput))
            else:
                print("Ashley: ", end="")
                print(responseToUser(ourInput, isname))

    else:
        indicator = False
        print("Ashley: I\'m leaving I hate you.")


"""
Name:           Farzin Amiri, Trishal Varma 
Class:          Human Language Technologies
Objective:     Creating a Chatbot with webscraped document to give informational responses to the user. 

New updated made July 21. 
"""



