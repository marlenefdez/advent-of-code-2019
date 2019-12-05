# advent of code, day 3, puzzle 2

def find_all_coordinates(wire_path):
    pass
def parse_input(wire_path):
    wire_paths = wire_path.replace(',',' ')
    wire_paths = wire_paths.split()

    all_pos = [] 
    dis = 0
    pt_dis = {}
    pos = (0,0) # start position
    for path in wire_paths:
        direction = path[0]
        steps     = int(path[1:])
        if direction == 'R':
            for _ in range(steps):
                pos = (pos[0], pos[1]+1)
                all_pos.append(pos)
                dis += 1
                if pos not in pt_dis:
                    pt_dis[pos] = dis

        if direction == 'L':
            for _ in range(steps):
                pos = (pos[0], pos[1]-1)
                all_pos.append(pos)
                dis += 1
                if pos not in pt_dis:
                    pt_dis[pos] = dis
        if direction == 'U':
            for _ in range(steps):
                pos = (pos[0]+1, pos[1])
                all_pos.append(pos)
                dis += 1
                if pos not in pt_dis:
                    pt_dis[pos] = dis
        if direction == 'D':
            for _ in range(steps):
                pos = (pos[0]-1, pos[1])
                all_pos.append(pos)
                dis += 1
                if pos not in pt_dis:
                    pt_dis[pos] = dis
    return pt_dis 

def manhattan_distance(tup):
    return abs(tup[0]) + abs(tup[1])

def total_steps(w1, w2):
    return w

if __name__ == "__main__":
    with open('input-aof-2019-12-03-01.txt','r') as prog:
        wires = prog.readlines()
        wire1 = wires[0]
        wire2 = wires[1]

        pos_wire1 = parse_input(wire1)
        pos_wire2 = parse_input(wire2)

        intersections = set(pos_wire1.keys()).intersection(set(pos_wire2.keys()))
        all_steps_dis = []
        all_steps_dis = [pos_wire1[inter] + pos_wire2[inter] for inter in intersections]
        print('The shortest step distance is {}'.format(min(all_steps_dis)))


