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


def gettotalcards(winners: list, scratch_cards: list):
    copies = [0] * len(winners)
    for i, card in enumerate(winners):
        winner_nums = list(set(card) & set(scratch_cards[i]))
        if len(winner_nums) > 0:
            for copy in range(1, len(winner_nums)+1):
                copies[i+copy] = copies[i+copy] + 1 + copies[i]
    return len(winners) + sum(copies)


print(gettotalcards(winning_numbers, elf_cards))