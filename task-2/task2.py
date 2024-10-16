regular_symbols = ['+', '*', '?', '|']
pointer = 1
class command:
    def __init__(self, regular_expression_, first_ = -1, second_ = -1, letter_ = ''):
        self.regular_expression = regular_expression_
        self.first = first_
        self.second = second_
        self.letter = letter_
commands = [command("UNDEFINED")]

def parallel(regular_expression_):
    global pointer
    let = 0
    while let < len(regular_expression_):
        if let + 1 >= len(regular_expression_) or regular_expression_[let+1] not in regular_symbols:
            pointer += 1
            commands.append(command("char", -1, -1, regular_expression_[let]))
            let += 1
        elif regular_expression_[let+1] == '*':
            commands.append(command("S", pointer + 1, pointer + 3))
            commands.append(command("char", -1, -1, regular_expression_[let]))
            commands.append(command("J", pointer))
            pointer += 3
            let += 2
        elif regular_expression_[let+1] == '?':
            commands.append(command("S", pointer + 1, pointer + 2))
            commands.append(command("char", -1, -1, regular_expression_[let]))
            pointer += 2
            let += 2
        else:
            commands.append(command("char", -1, -1, regular_expression_[let]))
            commands.append(command("S", pointer, pointer + 2))
            pointer += 2
            let += 2


def check(regular_expression_, cur_char, command_id):
    while True:
        if command_id >= len(commands):
            return False
        if commands[command_id].regular_expression == "M":
            if cur_char == len(regular_expression_):
                return True
            return False
        if commands[command_id].regular_expression == "char":
            if cur_char < len(regular_expression_) and regular_expression_[cur_char] == commands[command_id].letter:
                cur_char += 1
                command_id += 1
            else:
                return False
        elif commands[command_id].regular_expression == "J":
            command_id = commands[command_id].first
        else:
            return check(regular_expression_, cur_char, commands[command_id].first) or check(regular_expression_, cur_char, commands[command_id].second)

def pre_processing(regular_expression_):
    new_regular_expression_ = ""
    for i in range(len(regular_expression_)):
        symbols = []
        if regular_expression_[i] not in regular_symbols:
            if i + 1 >= len(regular_expression_) or regular_expression_[i + 1] not in regular_symbols or regular_expression_[i + 1] == '|':
                new_regular_expression_ += regular_expression_[i]
                continue
            if regular_expression_[i + 1] == '?':
                symbols = ['+', '*']
            elif regular_expression_[i + 1] == '+':
                symbols = ['*', '?']
            flag = False
            i2 = i + 2
            while i2 < len(regular_expression_):
                if regular_expression_[i2] in regular_symbols:
                    break
                if regular_expression_[i2] != '|':
                    break
                flag = regular_expression_[i2] in symbols
                i2 += 1
            if flag:
                new_regular_expression_ += regular_expression_[i] + '*'
            else:
                new_regular_expression_ += regular_expression_[i:i+2]
        if regular_expression_[i] == '|':
            new_regular_expression_ += '|'
    return new_regular_expression_

def VM(file_name, input_string_from_autotests = False):
    global pointer
    global commands
    global regular_symbols
    regular_symbols = ['+', '*', '?', '|']
    commands = [command("UNDEFINED")]
    pointer = 1
    file = open(f'{file_name}.txt', 'r')
    regular_expression = pre_processing(file.readline())

    if (input_string_from_autotests == ""):
        string = ""
    elif not(input_string_from_autotests):
        string = str(input())
    else:
        string = input_string_from_autotests

    variants = regular_expression.split('|')
    cur_char = 0
    for i in range(len(variants) - 1):
        if i + 2 == len(variants):
            commands[cur_char] = command("S", pointer)
            parallel(variants[i])
            commands.append(command("UNDEFINED"))
            commands[cur_char].second = pointer + 1
            tmp = pointer
            pointer += 1
            parallel(variants[i + 1])
            commands.append(command("M"))
            commands[tmp] = command("J", pointer)
            break
        commands[cur_char] = command("S", pointer)
        parallel(variants[i])
        commands[cur_char].second = pointer + 1
        commands.append(command("J", pointer + 2))
        commands.append(command("UNDEFINED"))
        commands.append(command("M"))
        cur_char = pointer + 1
        pointer += 3
    if len(variants) == 1:
        commands.pop()
        pointer -= 1
        parallel(variants[0])
        commands.append(command("M"))
    
    if check(string, 0, 0):
        return True
    return False