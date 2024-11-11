# 1. Implement a simple rule-based Text tokenizer for the English language using regular
#    expressions. Your tokenizer should consider punctuations and special symbols as
#    separate tokens. Contractions like "isn't" should be regarded as 2 tokens- "is" and "n't".
#    Also identify abbreviations (eg, U.S.A) and internal hyphenation (eg. ice-cream), as
#    single tokens.
import re

class Tokenizer:

    def __init__(self):
        
        self.tokens = {}
        self.special_tokens = {}
        self.cflag = True

    def insertIN(self,ikey,ivalue1,ivalue2,pos='e'):
        """
        logic of inserting
        "[abc]" = -0.99 (")|-0.98([)|0.00(abc)|0.98(])|0.99(")"""
        
        if pos == "e": # end 
            value = 99/100
            ikey2 = ikey + value
            check = True
            while check:
                if ikey2 in self.tokens.keys():
                    value = value - 1/100
                    ikey2 = ikey + value
                else: check = False

            self.tokens[ikey] = ivalue1
            self.tokens[ikey2] = ivalue2
            self.special_tokens[ikey]=ivalue1
        else: # beginning
            value = -99/100
            ikey2 = ikey + value
            check = True
            while check:
                if ikey2 in self.tokens.keys():
                    value = value + 1/100
                    ikey2 = ikey + value
                else: check = False
            self.tokens[ikey2] = ivalue1
            self.tokens[ikey] = ivalue2
            self.special_tokens[ikey]=ivalue2

    def applyRules(self):

        for i,word in self.special_tokens.items():

            # rule 2: split by ending punctuation
            if re.search(r'[,\"\'\-?:!;]$', word):
                n= len(word)
                self.insertIN(i,word[:n-1] ,word[-1])
                self.cflag = True
                word = self.special_tokens[i] # avoid repetition

            # rule 3: split by starting punctuation
            if re.search(r'^[,\"\'\-?:!;]', word):
                n= len(word)
                self.insertIN(i,word[0], word[1:n],"s")
                self.cflag = True
                word = self.special_tokens[i]

    def tokenize(self, text):

        # rule 1: split by whitespace
        words = re.split(r'\s+', text)
        # dictionarize to maintain order
        self.tokens = {float(i):word for i,word in enumerate(words)}

        # take special characters into another dict
        for i,word in self.tokens.items():
            if re.search(r'\W', word):
                self.special_tokens[i] = word

        # recurssively applying rule 2 & 3
        while self.cflag:
            self.cflag = False
            self.applyRules()

        for i,word in self.special_tokens.items():
        # rule 4: split for contractions
            if re.search(r'\'(m|s|re|d|ve|ll)', word):
                n= len(word)
                match = re.search(r'\'(m|s|re|d|ve|ll)', word)
                pos = match.start()
                self.insertIN(i,word[0:pos], word[pos:])
            # rule 5: split for n't
            if re.search(r'n\'t', word):
                n= len(word)
                match = re.search(r'n\'t', word)
                pos = match.start()
                self.insertIN(i,word[0:pos], word[pos:])
        return self.tokens

if __name__ == "__main__":
    tokenizer = Tokenizer()
    # text = "I'm really surprized!!! You're a R.A.W agent?"
    # text = "He doesn't care about ice-creams, he's strict diet; You also know that!"
    # text = "1, 2, 3 Stop lies like "pi is not 3.14", please???"
    print(" ")
    print("            Simple Text Tokenizer")
    print("           -----------------------")
    text = input("Please enter the string for tokenization: ")

    tokens = tokenizer.tokenize(text)
    print("Tokenized text: ",end='')
    for i in sorted(tokens):
        print(tokens[i],'|', end=' ')
    print()
    print(" ")
