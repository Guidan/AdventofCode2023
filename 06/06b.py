Time = 44707080
Distance = 283113411341491


def getrecordtimes(time: int, distance: int):
    num_ways = 0
    for k in range(1, time):
        if (k*(time-k)) > distance:
            num_ways = num_ways + 1
    return num_ways


print(getrecordtimes(Time, Distance))