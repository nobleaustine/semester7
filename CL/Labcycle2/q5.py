# 5. Design and implement a statistical spell checker for detecting and correcting non-word
#   spelling errors in English, using the bigram language model. Your program should do the
#   following:
#   a. Tokenize the corpus and create a corpus of unique words.
#   b. Create a bi-gram frequency table for all possible counts in the corpus.
#   c. Scan the given input text to identify the non-word spelling errors
#   d. Generate the candidate list using 1 edit distance from the misspelled words
#   e. Suggest the best candidate word by calculating the probability of the given sentence using the bigram LM.

import re
from collections import defaultdict
import math

global counts

def tokenize(text): return re.findall(r'\w+', text.lower())

def edit1d(word):

    global counts
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    candidates = [x for x in set(deletes + transposes + replaces + inserts) if x in counts]
    return candidates

def bigramify(corpus):

    counts = defaultdict(int)
    for i in range(len(corpus) - 1):
        if corpus[i] not in counts:
            counts[corpus[i]] = defaultdict(int)
        if corpus[i + 1] not in counts[corpus[i]]:
            counts[corpus[i]][corpus[i + 1]] = 1
        else:
            counts[corpus[i]][corpus[i + 1]] += 1    
    return counts

def corrector(sentence):
    global counts 
    a = 0.01  
    corrected_senentce = ""
    for i,word in enumerate(sentence):
        values={}
        if word not in counts:
            candidates = edit1d(word)
            for candidate in candidates:
                pb_a = math.log(counts[candidate][sentence[i+1]]+a)/(len(counts[candidate])+a*len(counts))
                pb_b = math.log(counts[sentence[i-1]][candidate]+a)/(len(counts[sentence[i-1]])+a*len(counts))
                values[candidate] = pb_a + pb_b
            value = max(values, key=values.get)    
            corrected_senentce += value + " "
        else:
            corrected_senentce += word + " "
    return corrected_senentce


def main():
    global counts

    # they are spelaing it wrong
    # the quik brown fox jumps over wall
    # he isi a really goood man
    # all teh best for the exam
    print(" ")
    print("        Bigram Statistical Spell Checker")
    flag = 'y'
    with open('./corpus.txt', 'r') as file:
            corpus = file.read()
    corpus = tokenize(corpus)
    counts = bigramify(corpus)
    while flag == 'y':
        text = input("Enter the test sentence: ")
        text = tokenize(text)
        corrected_text = corrector(text)
        print("Corrected sentence: ", corrected_text)
        flag = input("Continue? (y/n): ")
        print(" ")

    

    
    
if __name__ == "__main__":
    main()

    