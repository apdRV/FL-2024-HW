import collections

start_states = []
end_states = []
states_quantity = -1
alphabet_size = -1
graph =  []
graph1 = []

minimized_start_states = []
minimized_end_states = []
minimized_states_quantity = -1
minimized_graph = []

def reading_from_file(file_name):
    global start_states
    global end_states
    global graph
    global graph1
    global states_quantity
    global alphabet_size

    file_in = open(f'{file_name}.txt', 'r')
    start_states = []
    end_states = []

    states_quantity = int(file_in.readline())
    alphabet_size = int(file_in.readline())

    start_states = list(map(int, file_in.readline().split()))
    end_states = list(map(int, file_in.readline().split()))

    graph =  [[-1 for _ in range(alphabet_size)] for _ in range(states_quantity)]
    graph1 = [[-1 for _ in range(states_quantity)] for _ in range(states_quantity)]

    for line in file_in:
        from_state, symbol, to_state = map(int, line.split()) 
        graph[from_state][symbol] = to_state
        graph1[to_state][from_state] = symbol
    
    file_in.close()

def add_new_edges(from1, from2, graph2, q):
    global start_states
    global end_states
    global graph
    global graph1
    global states_quantity
    global alphabet_size

    for i in range (states_quantity):
        for j in range (states_quantity):
            first_st = graph1[from1][i]
            second_st = graph1[from2][j]
            if (first_st != -1 and second_st != -1 and graph2[i][j] == "EMPTY"):
                graph2[i][j] = -2
                graph2[j][i] = -2
                q.append((i, j))


def delete_unaccessible_states():
    v_st = start_states[0]
    used = [0 for _ in range(start_states)]
    def dfs(v):
        if (used[v]):
            return
        used[v] = 1
        for i in range(alphabet_size):
            for j in graph[v][i]:
                dfs(j)
    dfs(v_st)
    for i in range (states_quantity):
        if used[i] == 0:
            for j in range(alphabet_size):
                graph[i][j].clear()


def minimization(file_name = False):
    global start_states
    global end_states
    global graph
    global graph1
    global states_quantity
    global alphabet_size
    global minimized_start_states
    global minimized_end_states
    global minimized_graph
    global minimized_states_quantity

    if (file_name != False):
        reading_from_file(file_name)

    murrr_table = [["EMPTY" for _ in range(states_quantity)] for _ in range(states_quantity)]
    used = [-1 for i in range (states_quantity)]
    deque = collections.deque([])

    for state in end_states:
        for i in range (0, states_quantity):
            if i not in end_states:
                murrr_table[i][state] = -1
                murrr_table[state][i] = -1
                add_new_edges(i, state, murrr_table, deque)

    while deque:
        state1, state2 = deque.popleft()
        for i in range (alphabet_size):
            state1_1 = graph[state1][i]
            state2_2 = graph[state2][i]
            if (state1_1 != state2_2):
                if ((state1_1 == -1 or state2_2 == -1) and (not(state1_1 == -1 and state2_2 == -1))):
                    murrr_table[state1][state2] = i
                    murrr_table[state2][state1] = i
                    add_new_edges(state1, state2, murrr_table, deque)
                if (murrr_table[state1_1][state2_2] != -2):
                    murrr_table[state1][state2] = i
                    murrr_table[state2][state1] = i
                    add_new_edges(state1, state2, murrr_table, deque)
    for i in range (states_quantity):
        for j in range (states_quantity):
            if (i != j):
                if (i in end_states and j in end_states and murrr_table[i][j] == "EMPTY"):
                    murrr_table[i][j] = -2
                    murrr_table[j][i] = -2
    new_start_states = []
    new_end_states = []
    new_states_quantity = 0
    tmp = []
    for i in range (states_quantity):
        if used[i] == -1:
            new_index = new_states_quantity
            new_states_quantity += 1
            tmp.append(i)
            used[i] = new_index
            if (i == start_states[0]):
                new_start_states.append(new_index)
            if i in end_states:
                new_end_states.append(new_index)
            for j in range (i, states_quantity):
                if (murrr_table[i][j] == -2 or i == j):
                    used[j] = new_index
    new_graph = [[-1 for _ in range (alphabet_size)] for _ in range(new_states_quantity)]
    for i in range(new_states_quantity):
        for j in range (alphabet_size):
            if (murrr_table[tmp[i]][j] != -1):
                indexfortmpe = murrr_table[tmp[i]][j]
                if murrr_table[tmp[i]][j] == "EMPTY":
                    indexfortmpe = -3
                tmpe = used[indexfortmpe]
            new_graph[i][j] = tmpe
    minimized_graph = new_graph
    minimized_states_quantity = new_states_quantity
    minimized_end_states = new_end_states
    minimized_start_states = new_start_states

def write_into_file_minimized_graph(file_name):
    file_out = open(f'{file_name}-ans.txt', 'w+')
    file_out.write(f'{minimized_states_quantity}\n')
    file_out.write(f'{alphabet_size}\n')
    file_out.write(f'{minimized_start_states[0]}\n')
    for end_state in minimized_end_states:
        file_out.write(f'{end_state} ')
    file_out.write('\n')
    for i in range (minimized_states_quantity):
        for j in range (alphabet_size):
            if minimized_graph[i][j] != -1:
                file_out.write(f'{i} {j} {minimized_graph[i][j]}\n')
    
    file_out.close()

def is_accept_all_strings():
    global alphabet_size
    global minimized_start_states
    global minimized_end_states
    global minimized_graph
    global minimized_states_quantity

    all_states_quantity = 1
    all_alphabet_size = alphabet_size
    all_start_states = [0]
    all_end_states = [1]
    all_graph = [[0 for _ in range (all_alphabet_size)] for _ in range(all_states_quantity)]

    minimized_end_states_copy = minimized_end_states
    minimized_start_states_copy = minimized_start_states
    minimized_graph_copy = minimized_graph
    minimized_states_quantity_copy = minimized_states_quantity

    if (minimized_states_quantity != 1):
        return False
    new_list = [1]
    for i in range (minimized_states_quantity):
        flag = 1
        for j in range (alphabet_size):
            if (minimized_graph[i][j] != 1):
                flag = 0
                break
            if flag:
                return True
    return False



                    


