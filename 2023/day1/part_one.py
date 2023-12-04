import regex as re
from shared import util

"""
    2023 Day 1: Trebuchet?!
    https://adventofcode.com/2023/day/1
"""

# Example Data
test_data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

# Example Result
test_result = 142


# Solution
def solution(case):
    match = re.findall(r'\d', case)
    if not match:
        return 0
    else:
        first_number = match[0][0]
        last_number = match[-1][0]
        return int(first_number + last_number)


# Check Solution
util.check_solution(solution, test_data, test_result)

# Execute Solution
result = util.run_solution(solution)

print("Result: " + str(result))
