"""
Name:           Trishal Varma
Human Language Technologies
Objective:      Create a Word Guessing Game using library anat19.txt
"""
import random
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def printList(listIn):
    for c in listIn:
        print(c, end=' ')
# Compare list with the words for the game step.
def compareListEqual(my_list, chosen_word):
    for i in range(len(my_list)):
        if my_list[i] != chosen_word[i]:
            return False
    return True

# Step 1
    # Downloaded anat19 and opened it (added error code), used strip to read and get the words
def main():
    fileName = 'anat19.txt'
    try:
        with open(fileName) as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            words = []
            for record in content:
                records = record.split(" ");
                for word in records:
                    words.append(word.strip())
    except:
        print("Error in opening file")
        return
# Step 2
    # Reading input as raw text. Calculated the lexical diversity of the tokenized
    # text.
    file = open("anat19.txt").read()

    tokens = nltk.word_tokenize(file)
    num = len(set(tokens))/len(tokens)
    print("\nThe lexical diversity is {:0.2f}".format(num)) #******

# Step 3
    # A) tokenize lower-case raw text, reduce to only alpha. Length greater than 5
    tokens = [t.lower() for t in tokens if t.isalpha() and t not in stopwords.words('english') and len(t)>5]

    # B) getting Lemma of tokens using set line 56. unique.
    WNL = WordNetLemmatizer()
    lemmas = (WNL.lemmatize(t) for t in tokens)
    unique = list (set(lemmas))
    print("The number for unique lemmas are: ", len(unique))

    #C) POS tagging from ex.
    tags = nltk.pos_tag(unique)
    print("The 20 tags are:", tags[:20])

    #D) list of lemmas that are nouns
    import re
    nouns = [unique for unique in tags if re.search('NN.*', unique[1])]

    # E) print the number of tokens and nouns.
    print("Number of tokens is: ", len(tokens))
    print("Number of nouns is: ", len(nouns))


# Step 4
    # Dictionary of nouns and counts, saved in a list ot be used for the game.
    noun = {t:tokens.count(t) for t in tokens}
    nounDict = {}

    for n in noun:
        nounDict[n] = tokens.count(n)

    nounsSort = sorted(nounDict, key=nounDict.get, reverse=True)
    wordPool = nounsSort[:50]
    print(nounDict)


# Step 5
    # Guessing game, has 10 chances to get the word right.
    chance = 13
    print("\nYou have", chance, " chances. Guess all the letters!!")

    chosen_word = random.choice(wordPool)
    print(" For Testing, word is:", chosen_word)

    round = 0
    totalGuess = 0
    gameOver = False
    while True:
        my_list = []
        round += 1
        print("ROUND ", round)
        # Using _ for blank spaces. as shown in requirement
        for i in range(len(chosen_word)):
            my_list.append("_")
        print("The answer so far is ", end = "")
        printList(my_list)

        found = False;
        for i in range(chance):
            user_input = input("\nGuess a letter: ").lower()
            # Terminating the game if they put a "!"
            if user_input[0] == '!':

                gameOver = True
                break
            foundCurrent = False
            for k in range(len(chosen_word)):
                if user_input == chosen_word[k]:
                    foundCurrent = True
                    my_list[k] = chosen_word[k]
            if foundCurrent:
                print("Correct!")
            else:
                 print("Sorry!! Try Again! ")

            print("The answer so far is ", end="")
            printList(my_list)
            if compareListEqual(my_list, chosen_word):
                print('\nGREAT! You found the word ' + chosen_word + ".")
                found = True;
                totalGuess += 1
                break

        if not found:
            print("\nSorry! Wrong Answer, the word was : " + chosen_word + ". Play with us again!")
        if gameOver:
            break
    print("Total round played: ", round)
    print("Correct guesses: ", totalGuess)
    return tokens, nouns
main()


"""
Name:           Trishal Varma
Date:           September 4th, 2020
Class:          Human Language Technologies
Professor:      Karen Mazidi
Objective:      Create a Word Guessing Game using library anat19.txt
"""

