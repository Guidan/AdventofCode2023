with open("./input.txt") as file:
    map_input = file.readlines()

instructions = [*map_input[0]]
instructions.pop()
map_input = map_input[2::]
map_list = {}
for row in map_input:
    map_list[row[0:3]] = [row[7:10], row[12: 15]]


def getnumsteps(map_list: dict, instructions: list):
    curr_step = 'AAA'
    steps = 0
    while curr_step != 'ZZZ':
        for instruction in instructions:
            steps += 1
            match instruction:
                case 'L':
                    curr_step = map_list.get(curr_step)[0]
                case 'R':
                    curr_step = map_list.get(curr_step)[1]
                case _:
                    print("error")
            if curr_step == 'ZZZ':
                break
    return steps


print(getnumsteps(map_list, instructions))
