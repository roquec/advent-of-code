import math

import regex as re
from shared import util, matrix

"""
    2023 Day 7: Camel Cards
    https://adventofcode.com/2023/day/7
"""

# Example Data
test_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# Example Result
test_result = 6440


# Solution
def identify_poker_hand(hand):
    card_counts = {}
    for card in hand:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1

    counts = sorted(card_counts.values(), reverse=True)

    if 5 in counts:
        return "L"
    elif 4 in counts:
        return "K"
    elif counts == [3, 2]:
        return "J"
    elif 3 in counts:
        return "I"
    elif counts == [2, 2, 1]:
        return "H"
    elif 2 in counts:
        return "G"
    else:
        return "F"


def process_hand(hand):
    hand_type = identify_poker_hand(hand)

    processed_hand = hand_type + hand.replace("A", "E").replace("K", "D").replace("Q", "C").replace("J", "B").replace("T", "A")

    return processed_hand


def solution(data):
    lines = data.split('\n')

    hands = []

    for index, line in enumerate(lines):
        hand = line.split(' ')[0]
        bid = line.split(' ')[1]
        processed_hand = process_hand(hand)
        hands.append({"hand": hand, "bid": bid, "processed_hand": processed_hand})

    sorted_hands = sorted(hands, key=lambda x: x['processed_hand'])

    total = 0

    for index, hand in enumerate(sorted_hands):
        total += int(hand['bid']) * (index + 1)

    return total


# Check Solution
util.check_solution(solution, test_data, test_result, util.one_case)

# Execute Solution
result = util.run_solution(solution, util.one_case)

print("Result: " + str(result))
