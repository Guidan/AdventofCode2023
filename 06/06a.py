Time = [44,70,70,80]
Distance = [283, 1134, 1134, 1491]


def getrecordtimes(time: list, distance: list):
    total = 1
    for i, record in enumerate(time):
        num_ways = 0
        for k in range(1, record):
            if (k*(record-k)) > distance[i]:
                num_ways = num_ways + 1
        total = total * num_ways
    return total


print(getrecordtimes(Time, Distance))