# q0.add_transition([r"[A-Za-z]"], [q1])
# q1.add_transition([r"[aeou]",r"[y]",r"[b-df-j-np-tv-xz]"], [q2,q3,q5])
# q2.add_transition([r"[a-xz]",r"[y]"], [q1,q3])
# q3.add_transition([r"[a-rt-z]",r"[s]"], [q1,q4])
# q4.add_transition([r"[a-z]"], [q1])
# q5.add_transition([r"[a-df-hj-xz]",r"[ye]",r"[i]"], [q1,q3,q5])
# q6.add_transition([r"[A-Za-z]"], [q1])
import re
if re.search(r"[/]","/"):
    print("yahooooo")