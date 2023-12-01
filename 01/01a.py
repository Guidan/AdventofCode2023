with open("./input.txt") as file:
    code = file.readlines()


def getcalibration(string: str):
    first_num = ""
    last_num = ""
    for char in string:
        if char.isdigit():
            if first_num == "":
                first_num = char
            last_num = char
    return int(first_num + "" + last_num)


total = 0
for line in code:
    total = total + getcalibration(line)
print(total)
