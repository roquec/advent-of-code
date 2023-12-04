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
test_result = 4361


# Set up

# Solution
def check_number(lines, number, row_index, col_index):
    surrounding_chars = []
    digits = len(number)
    if row_index-1 >= 0:
        if col_index-1 >= 0:
            surrounding_chars.append(lines[row_index-1][col_index-1])
        surrounding_chars.append(lines[row_index-1][col_index:col_index+digits])
        if col_index+digits+1 < len(lines[row_index-1]):
            surrounding_chars.append(lines[row_index-1][col_index+digits])

    if col_index - 1 >= 0:
        surrounding_chars.append(lines[row_index][col_index - 1])
    if col_index + digits + 1 < len(lines[row_index]):
        surrounding_chars.append(lines[row_index][col_index + digits])

    if row_index+1 < len(lines):
        if col_index-1 >= 0:
            surrounding_chars.append(lines[row_index+1][col_index-1])
        surrounding_chars.append(lines[row_index+1][col_index:col_index+digits])
        if col_index+digits+1 < len(lines[row_index+1]):
            surrounding_chars.append(lines[row_index+1][col_index+digits])

    if re.search(r'[^A-Za-z0-9.\s]', ''.join(surrounding_chars)):
        return True
    else:
        return False


def solution(case):
    lines = case.split('\n')
    total = 0
    for line_index, line in enumerate(lines):
        matches = re.finditer(r'\d+', line)
        numbers = [(match.group(), match.start()) for match in matches]

        for number in numbers:
            if check_number(lines, number[0], line_index, number[1]):
                total += int(number[0])

    return total


# Check Solution
util.check_solution(solution, test_data, test_result, util.one_case)

# Execute Solution
result = util.run_solution(solution, util.one_case)

print("Result: " + str(result))
