from task2 import nfa_to_dfa

# TEST 1
nfa_to_dfa("tests/test1")
t1 = open('tests/test1-ans.txt').read()
t2 = open('tests/test1.sol').read()
assert(t1 == t2)

# TEST 2
nfa_to_dfa("tests/test2")
t1 = open('tests/test2-ans.txt').read()
t2 = open('tests/test2.sol').read()
assert(t1 == t2)

# TEST 3
nfa_to_dfa("tests/test3")
t1 = open('tests/test3-ans.txt').read()
t2 = open('tests/test3.sol').read()
assert(t1 == t2)