file = open('in.txt', 'r')

start_states = []
end_states = []

states_quantity = int(file.readline())
alphabet_size = int(file.readline())

start_states = list(map(int, file.readline().split()))
end_states = list(map(int, file.readline().split()))

for line in file:
    symbol, from_state, to_state = map(int, line.split()) 


file.close()

