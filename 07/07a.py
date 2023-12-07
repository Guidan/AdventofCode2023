from collections import Counter
with open("./input.txt") as file:
    hands = file.readlines()
SORT_KEY = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def getcardvalue(card: str):
    if card.isdigit():
        return int(card)
    else:
        return SORT_KEY.get(card)


def gettotalrank(hands: list):
    hand_list = []
    total = 0
    for line in hands:
        hand, bet = line.split()
        hand_list.append(Hand(hand, bet))
    hand_list = sorted(hand_list, key=lambda x: (x.hand_value, x.first_card, x.sec_card, x.third_card, x.fourth_card,
                                                 x.fifth_card))
    for rank, hand in enumerate(hand_list):
        total = total + (hand.bet * (rank + 1))
    return total


class Hand:
    def __init__(self, hand_str: str, bet: int):
        self.hand = hand_str
        self.bet = int(bet)
        self.hand_map = Counter([*hand_str])
        self.first_card = getcardvalue(hand_str[0])
        self.sec_card = getcardvalue(hand_str[1])
        self.third_card = getcardvalue(hand_str[2])
        self.fourth_card = getcardvalue(hand_str[3])
        self.fifth_card = getcardvalue(hand_str[4])
        match len(self.hand_map):
            case 1:
                self.hand_value = 7
            case 2:
                if list(self.hand_map.values())[0] in [1, 4]:
                    self.hand_value = 6
                else:
                    self.hand_value = 5
            case 3:
                num_pairs = 0
                for hand_count in self.hand_map.values():
                    if hand_count == 2:
                        num_pairs += 1
                if num_pairs == 2:
                    self.hand_value = 3
                else:
                    self.hand_value = 4
            case 4:
                self.hand_value = 2
            case 5:
                self.hand_value = 1

    def __str__(self):
        return str(str(self.hand_value) + ":" + self.hand + ":" + str(self.bet))

    def __repr__(self):
        return repr((self.hand_value, self.hand))


print(gettotalrank(hands))
