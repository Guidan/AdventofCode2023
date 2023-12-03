with open("./input.txt") as file:
    schematic = file.readlines()

SPECIAL_CHARS = "!@#$%^&*()-+?_=,<>/"


def get_sum(schem: list):
    total = 0
    for i, row in enumerate(schem):
        current_number = ""
        is_needed = False
        for k, char in enumerate(row):
            if char.isdigit():
                current_number = current_number + char
                if i > 0:
                    if any(c in SPECIAL_CHARS for c in schem[i-1][k-1:k+2]):
                        is_needed = True
                if any(c in SPECIAL_CHARS for c in row[k-1:k+2]):
                    is_needed = True
                if i < (len(schem)-1):
                    if any(c in SPECIAL_CHARS for c in schem[i+1][k-1:k+2]):
                        is_needed = True
            else:
                if is_needed:
                    total = total + int(current_number)
                    is_needed = False
                    current_number = ""
                else:
                    is_needed = False
                    current_number = ""
    return total


print(get_sum(schematic))
