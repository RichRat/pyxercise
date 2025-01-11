import re

from util.timing import timed_run

def advent_17_step_1():
    with open('../resources/advent/17_input.txt') as list_file:
       lines = [ line for line in list_file.read().split("\n")]

    regs = {}
    program = []

    for line in lines:
        if 'Register' in line:
            v = int(re.findall(r"\d+$", line)[0])
            r = re.findall(r"[ABC]", line)[0]
            regs[r] = v
        elif 'Program' in line:
            program = [ int(n) for n in re.findall(r"\d", line) ]

    def combo_op(op):
        return op if op <= 3 else regs['ABC'[op - 4]]

    out = []
    i = 0
    while i < len(program):
        op = program[i + 1]
        match(program[i]):
            case 0: regs['A'] >>= combo_op(op) #adv
            case 1: regs['B'] ^= op #bxl
            case 2: regs['B'] = combo_op(op) % 8 #bst
            case 3: i = i if regs['A'] == 0 else op - 2 #jnz
            case 4: regs['B'] = regs['B'] ^ regs['C'] #bxc
            case 5: out.append(combo_op(op) % 8) #out
            case 6: regs['B'] = regs['A'] >> combo_op(op) #bdv
            case 7: regs['C'] = regs['A'] >> combo_op(op) #cdv

        i += 2

    print("Result " + ",".join([ str(n) for n in out]))

def advent_17_step_2():
    with open('../resources/advent/17_input.txt') as list_file:
       lines = [ line for line in list_file.read().split("\n")]

    program = []

    for line in lines:
        if 'Program' in line:
            program = [ int(n) for n in re.findall(r"\d", line) ]

    def combo_op(op):
        return op if op <= 3 else regs['ABC'[op - 4]]

    def run_program():
        out_ind = 0
        i = 0
        while i < len(program):
            op = program[i + 1]
            match(program[i]):
                case 0: regs['A'] >>= combo_op(op) #adv
                case 1: regs['B'] ^= op #bxl
                case 2: regs['B'] = combo_op(op) % 8 #bst
                case 3: i = i if regs['A'] == 0 else op - 2 #jnz
                case 4: regs['B'] = regs['B'] ^ regs['C'] #bxc
                case 5:
                    out_val = combo_op(op) % 8
                    if program[out_ind] != out_val:
                        return False

                    out_ind += 1

                case 6: regs['B'] = regs['A'] >> combo_op(op)  # bdv
                case 7: regs['C'] = regs['A'] >> combo_op(op)  # cdv

            i += 2

        return out_ind == len(program)

    for a in range(0, 10**10):
        regs = {'A': a, 'B': 0, 'C': 0}
        if run_program():
            print("Result " + str(a))
            break

        if a % 100000 == 0:
            print(a)





print("step 1")
timed_run(advent_17_step_1)
# print("step 2")
# timed_run(advent_17_step_2)