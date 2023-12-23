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
def process_hand(hand):

    return


def solution(data):
    lines = data.split('\n')

    for index, line in enumerate(lines):
        hand = line.split(' ')[0]
        bid = line.split(' ')[1]

    lst = ['G32A3D', 'IA55B5', 'HDD677', 'HDABBA', 'ICCCBE']
    print(sorted(lst))

    return 0


# Check Solution
util.check_solution(solution, test_data, test_result, util.one_case)

# Execute Solution
result = util.run_solution(solution, util.one_case)

print("Result: " + str(result))
