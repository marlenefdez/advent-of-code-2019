# advent of code, day 2, puzzle 2
from itertools import combinations_with_replacement

def op(opcode, v1, v2):
    if opcode == 1:
        return v1 + v2
    if opcode == 2:
        return v1 * v2
    if opcode == 99:
        print(_prog)
        #raise SystemExit

def check_if_19690720(vals):
    if vals[0] == 19690720:
        print('The noun and verb to get 19690720 is {} and {}'.format(vals[1], vals[2]))
        print('The AOC input should be: {}'.format(100 * vals[1] +  vals[2]))
        raise SystemExit



def run_program(v1, v2, prog_inputs):
    inputs = list(prog_inputs) # this is to make a copy
    inputs[1] = v1 
    inputs[2] = v2

    for i in range(0,len(_prog),4):
        opcode = inputs[i]
        val1   = inputs[inputs[i+1]]
        val2   = inputs[inputs[i+2]]
        if opcode == 99:
            check_if_19690720(inputs)
            #raise SystemExit
            break
        result = op(opcode, val1, val2)
        inputs[inputs[i+3]] = result

if __name__ == "__main__":
    with open('input-aof-2019-12-02-01.txt','r') as prog:
        line = prog.readline()

    _prog = map(int,line.split(','))

    combos = combinations_with_replacement(range(0,100),2)
    for comb in combos:
        run_program(comb[0], comb[1], _prog)
        run_program(comb[1], comb[0], _prog)
