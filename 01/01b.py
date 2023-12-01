with open("./input.txt") as file:
    code = file.readlines()

numbers_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def getdigits(line: str):
    first_num = ""
    last_num = ""
    for i, char in enumerate(line):
        if char.isdigit():
            first_num = char
            break
        else:
            for chunk in range(1, 6):
                print(line[i: i+chunk])
                if line[i: i+chunk] in numbers_dict:
                    first_num = numbers_dict[line[i: i+chunk]]
                    break
            else:
                continue
            break
    for k, char in reversed(list(enumerate(line))):
        if char.isdigit():
            last_num = char
            break
        else:
            for chunk in range(1, 6):
                if line[k: k+chunk] in numbers_dict:
                    last_num = numbers_dict[line[k: k+chunk]]
                    break
            else:
                continue
            break
    return int(str(first_num) + "" + str(last_num))


total = 0
for string in code:
    total = total + getdigits(string)
print(total)