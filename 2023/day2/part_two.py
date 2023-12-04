import regex as re
from shared import util

"""
    2023 Day 2: Cube Conundrum
    https://adventofcode.com/2023/day/2
"""

# Example Data
test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

# Example Result
test_result = 2286


# Solution
def get_min_for_color(case, color):
    pattern = r'(\d+) ' + re.escape(color)
    numbers = [int(item) for item in re.findall(pattern, case)]
    return max(numbers)


def solution(case):
    red_min = get_min_for_color(case, "red")
    green_min = get_min_for_color(case, "green")
    blue_min = get_min_for_color(case, "blue")
    return red_min * green_min * blue_min


# Check Solution
util.check_solution(solution, test_data, test_result)

# Execute Solution
result = util.run_solution(solution)

print("Result: " + str(result))
