import re
from shared import util, matrix

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
def set_gears(gear_map, lines, number, row_index, col_index):
    surrounding_chars = []
    digits = len(number)

    surrounding_chars += matrix.matrix_range(lines, row_index-1, col_index-1, col_index + digits + 1, '.')
    surrounding_chars += matrix.matrix_range(lines, row_index, col_index-1, col_index + digits + 1, '.')
    surrounding_chars += matrix.matrix_range(lines, row_index+1, col_index-1, col_index + digits + 1, '.')

    matches = re.finditer(r'\*', ''.join(surrounding_chars))
    for gear in matches:
        gear_row = (gear.start() // (digits+2)) + (row_index - 1)
        gear_col = (gear.start() % (digits+2)) + (col_index - 1)
        key = f'{gear_row}_{gear_col}'

        if key in gear_map:
            gear_map[key] += [number]
        else:
            gear_map[key] = [number]


def solution(case):
    gear_map = {
    }

    lines = case.split('\n')
    total = 0
    for line_index, line in enumerate(lines):
        matches = re.finditer(r'\d+', line)
        numbers = [(match.group(), match.start()) for match in matches]

        for number in numbers:
            set_gears(gear_map, lines, number[0], line_index, number[1])

    for key, value in gear_map.items():
        if len(value) == 2:
            total += int(value[0]) * int(value[1])

    return total


# Check Solution
util.check_solution(solution, test_data, test_result, util.one_case)

# Execute Solution
result = util.run_solution(solution, util.one_case)

print("Result: " + str(result))
