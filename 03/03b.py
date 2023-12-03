with open("./input.txt") as file:
    schematic = file.readlines()


def get_sum(schem: list):
    total = 0
    gears_list = {}
    for i, row in enumerate(schem):
        current_number = ""
        connected_gear = None
        for k, char in enumerate(row):
            if char.isdigit():
                current_number = current_number + char
                if i > 0:
                    if schem[i-1][k-1] == "*":
                        connected_gear = str(i-1)+str(k-1)
                    if schem[i - 1][k] == "*":
                        connected_gear = str(i - 1) + str(k)
                    if schem[i - 1][k + 1] == "*":
                        connected_gear = str(i - 1) + str(k + 1)
                if i < len(schem)-2:
                    if schem[i+1][k - 1] == "*":
                        connected_gear = str(i+1) + str(k - 1)
                    if schem[i+1][k] == "*":
                        connected_gear = str(i+1) + str(k)
                    if schem[i+1][k + 1] == "*":
                        connected_gear = str(i+1) + str(k + 1)
                if schem[i][k - 1] == "*":
                    connected_gear = str(i) + str(k - 1)
                if schem[i][k] == "*":
                    connected_gear = str(i) + str(k)
                if schem[i][k + 1] == "*":
                    connected_gear = str(i) + str(k + 1)
            else:
                if current_number != "":
                    if connected_gear:
                        if gears_list.get(connected_gear):
                            total = total + (int(gears_list.get(connected_gear)) * int(current_number))
                        else:
                            gears_list[connected_gear] = current_number
                    current_number = ""
                    connected_gear = None

    return total


print(get_sum(schematic))
