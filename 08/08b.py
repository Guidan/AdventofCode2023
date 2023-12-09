import string, math
with open("./input.txt") as file:
    map_input = file.readlines()

instructions = [*map_input[0]]
instructions.pop()
map_input = map_input[2::]
map_list = {}
A_map = []
for row in map_input:
    if row[2] == 'A':
        A_map.append(row[0:3])
    map_list[row[0:3]] = [row[7:10], row[12: 15]]


def getnumsteps(map_list: dict, instructions: list, start: str):
    curr_step = start
    steps = 0
    while curr_step[-1] != 'Z':
        for instruction in instructions:
            steps += 1
            match instruction:
                case 'L':
                    curr_step = map_list.get(curr_step)[0]
                case 'R':
                    curr_step = map_list.get(curr_step)[1]
                case _:
                    print("error")
    return steps


A_count = []
for A in A_map:
    A_count.append(getnumsteps(map_list, instructions, A))
print(math.lcm(*A_count))
