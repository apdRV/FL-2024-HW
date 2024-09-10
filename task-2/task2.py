
def nfa_to_dfa(file_name):
    file_in = open(f'{file_name}.txt', 'r')
    
    states_quantity = int(file_in.readline())    
    alphabet_size = int(file_in.readline())
    
    start_states = list(map(int, file_in.readline().split()))
    end_states = list(map(int, file_in.readline().split()))
    
    graph =  [[[0 for _ in range(0)] for _ in range(alphabet_size)] for _ in range(states_quantity)]
    
    for line in file_in:
        from_state, symbol, to_state = map(int, line.split()) 
        graph[from_state][symbol].append(to_state)
    
    file_in.close()
    
    dfa_states = []
    dfa_transitions = {}
    dfa_start_state = tuple(sorted(start_states))
    dfa_states.append(dfa_start_state)
    unmarked_states = [dfa_start_state]
    dfa_end_states = set()
    
    while unmarked_states:
        current_state = unmarked_states.pop()
        dfa_transitions[current_state] = {}
        
        for symbol in range(alphabet_size):
            new_state = set()
            for nfa_state in current_state:
                new_state.update(graph[nfa_state][symbol])
            new_state = tuple(sorted(new_state))
            if new_state and new_state not in dfa_states:
                dfa_states.append(new_state)
                unmarked_states.append(new_state)
            dfa_transitions[current_state][symbol] = new_state
            if any(state in end_states for state in new_state):
                dfa_end_states.add(new_state)
    
    file_out = open(f'{file_name}-ans.txt', 'w+')
    file_out.write(f'{len(dfa_states)}\n')
    file_out.write(f'{alphabet_size}\n')
    file_out.write(''.join(map(str, dfa_start_state)) + '\n')
    for end_state in dfa_end_states:
        file_out.write(''.join(map(str, end_state)) + ' ')
        file_out.write('\n') 
    for state, transitions in dfa_transitions.items():
        for symbol, next_state in transitions.items():
            file_out.write(f'{"".join(map(str, state))} {symbol} {"".join(map(str, next_state))}\n')
    
    file_out.close()