# 2. Design and implement a Finite State Automata(FSA) that accepts English plural nouns
#    ending with the character ‘y’, e.g. boys, toys, ponies, skies, and puppies but not boies or
#    toies or ponys. (Hint: Words that end with a vowel followed by ‘y’ are appended with ‘s'
#    and will not be replaced with “ies” in their plural form).

import re

# state of FSA
class State():
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    # overloading [] for transition
    def __getitem__(self, symbol):
        for pattern,state in self.transitions.items():
            if re.match(pattern, symbol):
                return state
        
    def add_transition(self, patterns, states):
        for pattern,state in zip(patterns,states):
            self.transitions[pattern] = state
            
# Finite State Automata
class FSA():

    def __init__(self,states, alphabet, start, accept):
        self.states = states
        self.alphabet = alphabet
        self.start = start
        self.accept = accept

    def run(self, string):
        current_state = self.start
        print('-->', end='')
        for char in string:
            print(f'({current_state.name})--{char}-->', end='')
            current_state = current_state[char]
        if current_state in self.accept:
            print(f'(({current_state.name}))')
        else:
            print(f'({current_state.name})')
        print(" ")

        if current_state in self.accept:
            print("            --- Input Accepted ---")
        else:
            print("            --- Input Rejected ---")

def main():

    # setup for the FSA
    q0 = State('q0')
    q1 = State('q1')
    q2 = State('q2')
    q3 = State('q3')
    q4 = State('q4')
    q5 = State('q5')

    q0.add_transition([r"[aeiouAEIOU]",r"[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]"], [q1,q2])
    q1.add_transition([r"[aeiou]",r"[b-df-hj-np-tv-xz]",r"[y]"], [q1,q2,q3])
    q2.add_transition([r"[aeou]",r"[b-df-hj-np-tv-z]",r"[i]"], [q1,q2,q4])
    q3.add_transition([r"[aeou]",r"[b-df-hj-np-rt-z]",r"[i]",r"[s]"], [q1,q2,q4,q5])
    q4.add_transition([r"[aiou]",r"[b-df-hj-np-tv-xz]",r"[ey]"], [q1,q2,q3])
    q5.add_transition([r"[aeou]",r"[b-df-hj-np-tv-z]",r"[i]"], [q1,q3,q4])
    

    fsa = FSA([q0,q1,q2,q3,q4,q5], [r"[A-Za-z]"], q0, [q5])
    cflag = True
    print(" ")
    print("            Finite State Automata")
    while cflag:
        text = input("Please enter the input to the FSA: ")
        fsa.run(text)
        print(" ")
        cflag = input("Do you want to continue? (y/n): ") == 'y'

if __name__ == "__main__":
    # boys, toys, ponies, skies, and puppies but not boies toies or ponys
    main()
    print(" ")
   