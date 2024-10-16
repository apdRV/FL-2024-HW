import task1

# TEST 1
task1.minimization("tests/test1DFA")
task1.write_into_file_minimized_graph("tests/test1MINIMIZEDDFA")
t1 = open("tests/test1MINIMIZEDDFA-ans.txt").read()
t2 = open("tests/test1MINIMIZEDDFA.sol").read()
assert(t1 == t2)
assert(task1.is_accept_all_strings() == False)

# TEST 2
task1.minimization("tests/test2DFA")
task1.write_into_file_minimized_graph("tests/test2MINIMIZEDDFA")
t1 = open("tests/test2MINIMIZEDDFA-ans.txt").read()
t2 = open("tests/test2MINIMIZEDDFA.sol").read()
assert(t1 == t2)
assert(task1.is_accept_all_strings() == False)