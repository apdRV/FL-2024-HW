
def simulator(file_name, input_string_from_autotests = False):
    file = open(f'{file_name}.txt', 'r')

    start_states = []
    end_states = []

    states_quantity = int(file.readline())
    alphabet_size = int(file.readline())

    start_states = list(map(int, file.readline().split()))
    end_states = list(map(int, file.readline().split()))

    graph =  [[[0 for _ in range(0)] for _ in range(alphabet_size)] for _ in range(states_quantity)]

    def dfs(v, request, i):
        if i == len(request):
            if v in end_states:
                return True
            return False
        for x in graph[v][int(request[i])]:
            if dfs(x, request, i + 1):
                return True

    for line in file:
        from_state, symbol, to_state = map(int, line.split()) 
        graph[from_state][symbol].append(to_state)
    
    if not(input_string_from_autotests):
        input_string = str(input().strip())
    else:
        input_string = input_string_from_autotests

    file.close()

    for v in start_states:
        if (dfs(v, input_string, 0)):
            return True
    return False