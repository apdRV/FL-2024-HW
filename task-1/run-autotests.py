from task1 import simulator

# TEST 1
assert(simulator("tests/test1", "010101") == False)
assert(simulator("tests/test1", "00000000") == True)
assert(simulator("tests/test1", "01010100000000000001010101") == False)
assert(simulator("tests/test1", "010101111111111111111111111111111111100") == True)
assert(simulator("tests/test1", "0") == True)
assert(simulator("tests/test1", "1") == False)
assert(simulator("tests/test1", "11111111111110000") == True)

# TEST 2
assert(simulator("tests/test2", "2222222") == True)
assert(simulator("tests/test2", "1222022") == False)
assert(simulator("tests/test2", "0") == False)
assert(simulator("tests/test2", "1") == True)
assert(simulator("tests/test2", "2") == True)
assert(simulator("tests/test2", "221100210201020102") == False)
assert(simulator("tests/test2", "01111111111") == True)

# TEST 3
assert(simulator("tests/test3", "9") == True)
assert(simulator("tests/test3", "37819999999999999999999") == True)
assert(simulator("tests/test3", "97998") == False)
assert(simulator("tests/test3", "9348") == False)
assert(simulator("tests/test3", "28") == True)
assert(simulator("tests/test3", "3753") == True)
assert(simulator("tests/test3", "3753812312") == False)