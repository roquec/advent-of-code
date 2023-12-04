import regex as re
from shared import util

"""
    2023 Day 1: Trebuchet?!
    https://adventofcode.com/2023/day/1
"""

# Example Data
test_data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

# Example Result
test_result = 281


# Solution
number_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def solution(case):
    match = re.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine)', case, overlapped=True)
    if not match:
        return 0
    else:
        first_number = str(number_map.get(match[0], match[0]))
        last_number = str(number_map.get(match[-1], match[-1]))
        return int(first_number + last_number)


# Check Solution
util.check_solution(solution, test_data, test_result)

# Execute Solution
result = util.run_solution(solution)

print("Result: " + str(result))
