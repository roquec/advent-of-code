import regex as re
from shared import util

"""
    2023 Day 3: Gear Ratios
    https://adventofcode.com/2023/day/3
"""

# Example Data
test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

# Example Result
test_result = 467835


# Set up

# Solution
def solution(case):
    return 0


# Check Solution
util.check_solution(solution, test_data, test_result, util.one_case)

# Execute Solution
result = util.run_solution(solution, util.one_case)

print("Result: " + str(result))
