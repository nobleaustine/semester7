# 3. Design and implement a Finite State Transducer(FST) that accepts lexical forms of
#    English words(e.g. shown below) and generates its corresponding plurals, based on the
#    e-insertion spelling rule є => e / {x,s,z}^ __ s#
#    ^ is the morpheme boundary and #- word boundary

import re

# state of FST
class State():
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    # overloading [] for transition
    def __getitem__(self, symbol):
        for pattern,stateWritten in self.transitions.items():
            if re.match(pattern, symbol):
                state,written = stateWritten
                return state,written
        
    def add_transition(self, patterns,states,writtens):
        for pattern,state,written in zip(patterns,states,writtens):
            self.transitions[pattern] = (state,written)
            
# Finite State Automata
class FST():

    def __init__(self,states, alphabet, start, accept):
        self.states = states
        self.alphabet = alphabet
        self.start = start
        self.accept = accept

    def run(self, string):
        current_state = self.start
        output=''
        print('-->', end='')
        for char in string:
            if current_state.name!="deadstate":
                print(f'({current_state.name})', end='')
                current_state,letter = current_state[char]

                if letter=="=":
                    output+=char
                    letter = char
                elif letter=="ε":
                    letter="ε"
                else:
                    output+=letter
                print(f'--{char}:{letter}-->', end='')

        if current_state in self.accept:
            print(f'(({current_state.name}))')
        else:
            print(f'({current_state.name})')
        print(" ")

        if current_state in self.accept:
            print(f"            --- Plural Noun :{output} ---")
        else:
            print("            --- Invalid Intermediate Format ---")

def main():

    # setup for the FST
    q0 = State('q0')
    q1 = State('q1')
    q2 = State('q2')
    q3 = State('q3')
    q4 = State('deadstate')
    
    q0.add_transition([r"[a-rt-wy]",r"[\^#]",r"[zsx]"], [q0,q0,q1],["=","ε","="])
    q1.add_transition([r"[a-rt-wy]",r"[#]",r"[zsx]",r"[\^]"], [q0,q0,q1,q2],["=","ε","=","ε"])
    q2.add_transition([r"[s]",r"[a-rt-z]"], [q3,q4],["e","="])
    q3.add_transition([r"[#]",r"[a-z]"], [q0,q4],["s","="])
    
    fst = FST([q0,q1,q2,q3,q4,], [r"[A-Za-z\^#]"], q0, [q0])

    cflag = True
    print(" ")
    print("            Finite State Transducer")
    while cflag:
        text = input("Please enter the input to the FST: ")
        fst.run(text)
        print(" ")
        cflag = input("Do you want to continue? (y/n): ") == 'y'

if __name__ == "__main__":
    # boy^s#,buzz^s#,fox^s#,bus^s#
    main()
    print(" ")
   