import re
with open("./input.txt") as file:
    cards = file.readlines()

winning_numbers = []
elf_cards = []


for card in cards:
    numbers_before_pipe = re.search(r':\s*([\d\s]+)\s*\|', card).group(1)
    winning_numbers.append([int(num) for num in numbers_before_pipe.split()])
    numbers_after_pipe = re.search(r'\|\s*([\d\s]+)', card).group(1)
    elf_cards.append([int(num) for num in numbers_after_pipe.split()])


def getCardValue(card: list, winners: list):
    winner_list = list(set(card) & set(winners))
    value = 1
    if len(winner_list) == 0:
        return 0
    else:
        return value * 2**(max(len(winner_list) - 1, 0))


total = 0
for i, card in enumerate(elf_cards):
    total = total + getCardValue(card, winning_numbers[i])
print(total)