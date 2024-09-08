file = open('in.txt', 'r')

start_states = []
end_states = []

states_quantity = int(file.readline())
alphabet_size = int(file.readline())

start_states = list(map(int, file.readline().split()))
end_states = list(map(int, file.readline().split()))

for line in file:
    from_state, symbol, to_state = map(int, line.split()) 

input_string = str(input().strip())

file.close()

for symbol in input_string:
    print(symbol)
