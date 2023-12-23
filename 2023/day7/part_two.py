import math

import regex as re
from shared import util, matrix

"""
    2023 Day 6: Wait For It
    https://adventofcode.com/2023/day/6
"""

# Example Data
test_data = """Time:      7  15   30
Distance:  9  40  200"""

# Example Result
test_result = 71503


# Solution
def solve_race(time, record):
    lower_bound = (time - math.sqrt(time*time - (4 * record))) / 2
    upper_bound = (time + math.sqrt(time*time - (4 * record))) / 2

    lower_bound = math.floor(lower_bound) + 1
    upper_bound = math.ceil(upper_bound) - 1

    print(f'Race with time {time} and record {record} => lower_bound: {lower_bound}, upper_bound: {upper_bound}')
    return upper_bound - lower_bound + 1


def solution(data):
    lines = data.split('\n')

    time_data = lines[0]
    distance_data = lines[1]

    time = ''.join(re.findall(r'\d+', time_data))
    distance = ''.join(re.findall(r'\d+', distance_data))

    return solve_race(int(time), int(distance))


# Check Solution
util.check_solution(solution, test_data, test_result, util.one_case)

# Execute Solution
result = util.run_solution(solution, util.one_case)

print("Result: " + str(result))
