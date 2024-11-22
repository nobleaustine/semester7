# 6. Implement a text classifier for sentiment analysis using the Naive Bayes theorem. Use
#    Add-k smoothing to handle zero probabilities. Compare the performance of your
#    classifier for k values 0.25, 0.75, and 1

from matplotlib.cbook import pts_to_poststep
import pandas as pd
import re
from collections import defaultdict

global counts
counts = defaultdict(int)

def tokenize(text): return re.findall(r'\w+', text.lower())

def analyze(text,pos,neg,k=1):

    global counts
    p_pos = pos
    p_neg = neg
    p_count=0
    n_count =0
    N = len(counts)
    for sample in counts.values():
        p_count = p_count+sample["+"]
        n_count = n_count+sample["-"]

    words = tokenize(text)
     
    for word in words:
        p_pos = p_pos*((counts[word]['+']+k)/(p_count+k*N))
        p_neg = p_neg*((counts[word]['-']+k)/(n_count+k*N))

    if p_pos>p_neg:
        return "positive"
    else:
        return "negative"

def main():
    global counts

    with open('/home/jarvis/codebase_II/semester7/CL/Labcycle2/Sentiment Analysis Dataset.csv', mode='r', encoding='utf-8', errors='ignore') as file:
        data = pd.read_csv(file)
    pos = 0
    neg = 0
    N = 0
    for sentiment, sentence in zip(data['Sentiment'], data['SentimentText']):
        if sentiment == 1:
            pos+=1
        else:
            neg+=1
        N+=1
        words = tokenize(sentence)

        for word in words:
            if word not in counts:
                counts[word] = {'+': 0, '-': 0}
            else:
                if sentiment == 1:
                    counts[word]['+'] += 1
                else:
                    counts[word]['-'] += 1
    pos = pos/N
    neg = neg/N
    print(" ")
    print("        Statistical Sentiment Analysis")
    flag = 'y'
    while flag == 'y':
        text = str(input("Enter the test sentence: "))
        senti = analyze(text,pos,neg,k=1)
        print(f"This sentence is {senti}")
        flag = input("Continue? (y/n): ")
        print(" ")
    senti = analyze(text,pos,neg,k=1)
    
    
if __name__ == '__main__':
    main()