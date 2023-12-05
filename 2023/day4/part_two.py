import regex as re
from shared import util, matrix

"""
    2023 Day 4: Scratchcards
    https://adventofcode.com/2023/day/4
"""

# Example Data
test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

# Example Result
test_result = 30


# Set up

# Solution
def solve_card(case):
    total = 0
    data = case.split(':')[1]
    winning_data = data.split('|')[0]
    my_data = data.split('|')[1]

    winning_numbers = re.findall(r'\d+', winning_data)
    my_numbers = re.findall(r'\d+', my_data)

    for my_number in my_numbers:
        if my_number in winning_numbers:
            total += 1
    return total


def solution(case):
    total = 0
    cards = case.split('\n')
    card_values = {}
    card_numbers = {}
    for index, card in enumerate(cards):
        card_value = solve_card(card)
        card_values[index] = card_value
        card_numbers[index] = 1

    for index, card_value in card_values.items():
        for i in range(card_value):
            if index + i + 1 < len(card_numbers):
                card_numbers[index + i + 1] += card_numbers[index]

    for card_number in card_numbers.values():
        total += card_number

    return total


# Check Solution
util.check_solution(solution, test_data, test_result, util.one_case)

# Execute Solution
result = util.run_solution(solution, util.one_case)

print("Result: " + str(result))
