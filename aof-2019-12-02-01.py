# advent of code, day 2, puzzle 1

def op(opcode, v1, v2):
    if opcode == 1:
        return v1 + v2
    if opcode == 2:
        return v1 * v2
    if opcode == 99:
        print(_prog)
        raise SystemExit

with open('input-aof-2019-12-02-01.txt','r') as prog:
    line = prog.readline()

_prog = map(int,line.split(','))

# before running the program, replace position 1 with the value 12 and 
# replace position 2 with the value 2
_prog[1] = 12
_prog[2] = 2

for i in range(0,len(_prog),4):
    print(i)
    opcode = _prog[i]
    val1   = _prog[_prog[i+1]]
    val2   = _prog[_prog[i+2]]
    result = op(opcode, val1, val2)
    _prog[_prog[i+3]] = result

print('The val at pos 0 is: {}'.format(_prog[0]))

