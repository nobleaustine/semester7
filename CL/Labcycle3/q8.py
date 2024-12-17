# 8. Write a Python code to calculate bigrams from a given corpus and calculate the
#  probability of any given sentence

from collections import defaultdict
import re

def tokenize(text): return re.findall(r'\w+', text.lower())

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

with open("./files/corpus.txt") as f:
    corpus = f.read()

corpus = tokenize(corpus)
p = bigramify(corpus)

sen = "the quick brown fox jumps over the wall"

sentence = tokenize(sen)
a = 0.01
value = 0


print(" ")
print("Bigram Sentence Probability Calculation")
print(" ")
print("Bigram Probability")
value = sum(p[sentence[0]].values())
for i in range(1,len(sentence) - 1):
    value = value*(p[sentence[i-1]][sentence[i]]+a)/(sum(p[sentence[i-1]].values())+a*len(p))
    print(f"Probability of {sentence[i]} given {sentence[i-1]} is {value}")
print(" ")
print("Sentence: ",sen)
print(f"Probability of the sentence is {value}")
print(" ")
    
    
    

