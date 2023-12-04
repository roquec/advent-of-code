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
test_result = 8


# Set up
max_red = 12
max_green = 13
max_blue = 14


# Solution
def check_color(case, color, max_number):
    pattern = r'(\d+) ' + re.escape(color)
    numbers = re.findall(pattern, case)
    for number in numbers:
        if int(number) > max_number:
            return False
    return True


def solution(case):
    game_id = re.search(r'\d+', case).group(0)
    red_valid = check_color(case, "red", max_red)
    green_valid = check_color(case, "green", max_green)
    blue_valid = check_color(case, "blue", max_blue)

    if red_valid and green_valid and blue_valid:
        return int(game_id)
    else:
        return 0


# Check Solution
util.check_solution(solution, test_data, test_result)

# Execute Solution
result = util.run_solution(solution)

print("Result: " + str(result))
