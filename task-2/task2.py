
def nfa_to_dfa(file_name):
    file_in = open(f'{file_name}.txt', 'r')

    start_states = []
    end_states = []

    states_quantity = int(file_in.readline())
    alphabet_size = int(file_in.readline())

    start_states = list(map(int, file_in.readline().split()))
    end_states = list(map(int, file_in.readline().split()))

    graph =  [[[0 for _ in range(0)] for _ in range(alphabet_size)] for _ in range(states_quantity)]

    for line in file_in:
        from_state, symbol, to_state = map(int, line.split()) 
        graph[from_state][symbol].append(to_state)

    file_in.close()

    file_out = open(f'{file_name}.sol', 'w+')

    