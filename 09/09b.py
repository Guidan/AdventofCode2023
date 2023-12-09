with open("./input.txt") as file:
    sensor_input = file.readlines()

sensor_map = []
for row in sensor_input:
    sensor_map.append(list(map(int, row.split())))


def gethistory(map: list):
    curr_sequence = []
    total_sequence = [map]
    for i, num in enumerate(map):
        if i < len(map)-1:
            curr_sequence.append(map[i+1]-num)
    total_sequence.append(curr_sequence)
    while not all(value == 0 for value in curr_sequence):
        next_sequence = []
        for i, num in enumerate(curr_sequence):
            if i < len(curr_sequence)-1:
                next_sequence.append(curr_sequence[i+1]-num)
        curr_sequence = next_sequence
        total_sequence.append(curr_sequence)
    total_sequence.reverse()
    curr_interval = 0
    for i, seq in enumerate(total_sequence):
        if i < len(total_sequence)-1:
            next_num = total_sequence[i+1][0]
            curr_interval = next_num - curr_interval
    return curr_interval


total = 0
for sensor in sensor_map:
    total = total + gethistory(sensor)
print(total)