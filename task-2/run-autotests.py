import task2

# TEST 1
assert(task2.VM("tests/test1", "b") == False)
assert(task2.VM("tests/test1", "") == False)
assert(task2.VM("tests/test1", "a") == False)
assert(task2.VM("tests/test1", "ab") == True)
assert(task2.VM("tests/test1", "ba") == False)
assert(task2.VM("tests/test1", "aaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == True)

# TEST 2
assert(task2.VM("tests/test2", "s") == True)
assert(task2.VM("tests/test2", "") == False)
assert(task2.VM("tests/test2", "kkks") == True)
assert(task2.VM("tests/test2", "gd") == True)
assert(task2.VM("tests/test2", "goooood") == True)
assert(task2.VM("tests/test2", "bb") == True)

# TEST 3
assert(task2.VM("tests/test3", "") == True)
assert(task2.VM("tests/test3", "k") == True)
assert(task2.VM("tests/test3", "kk") == False)
assert(task2.VM("tests/test3", "bc") == True)
assert(task2.VM("tests/test3", "bcg") == True)
assert(task2.VM("tests/test3", "aaaaaaaabcjjjjjjjjjjjjg") == True)