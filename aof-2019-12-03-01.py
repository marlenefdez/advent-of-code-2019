# advent of code, day 3, puzzle 1

def find_all_coordinates(wire_path):
    pass
def parse_input(wire_path):
    wire_paths = wire_path.replace(',',' ')
    wire_paths = wire_paths.split()

    all_pos = []
    pos = (0,0) # start position
    for path in wire_paths:
        direction = path[0]
        steps     = int(path[1:])
        if direction == 'R':
            for _ in range(steps):
                pos = (pos[0], pos[1]+1)
                all_pos.append(pos)
        if direction == 'L':
            for _ in range(steps):
                pos = (pos[0], pos[1]-1)
                all_pos.append(pos)
        if direction == 'U':
            for _ in range(steps):
                pos = (pos[0]+1, pos[1])
                all_pos.append(pos)
        if direction == 'D':
            for _ in range(steps):
                pos = (pos[0]-1, pos[1])
                all_pos.append(pos)
    return set(all_pos)

def manhattan_distance(tup):
    return abs(tup[0]) + abs(tup[1])

if __name__ == "__main__":
    with open('input-aof-2019-12-03-01.txt','r') as prog:
        wires = prog.readlines()
        wire1 = wires[0]
        wire2 = wires[1]

        pos_wire1 = parse_input(wire1)
        pos_wire2 = parse_input(wire2)

        intersections = pos_wire1.intersection(pos_wire2)
        all_man_dis = [manhattan_distance(intersection) for intersection in intersections]
        print('The shortest Manhattan distance is {}'.format(min(all_man_dis)))


