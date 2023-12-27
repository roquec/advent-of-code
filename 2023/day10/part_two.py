import math

import regex as re
from shared import util, matrix

"""
    2023 Day 10: Pipe Maze
    https://adventofcode.com/2023/day/10
"""

# Example Data
test_data = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

# Example Result
test_result = 10


# Solution
def find_start(data, line_length):
    starting_char = "S"
    index = data.find(starting_char)
    row = index // line_length
    col = index % line_length
    return row, col


def solution(data):
    lines = data.splitlines()
    line_length = len(lines[0])

    row, col = find_start(data, line_length+1)

    print(f"Row: {row}, Col: {col}")

    left_char, right_char, top_char, bottom_char = ".", ".", ".", "."

    if row > 0:
        left_char = lines[row-1][col]
    if row < (line_length - 1):
        right_char = lines[row+1][col]
    if col > 0:
        top_char = lines[row][col-1]
    if col < (len(lines) - 1):
        bottom_char = lines[row][col+1]

    next_char = {"row": -1, "col": -1}
    if top_char in ["|", "7", "F"]:
        next_char = {"row": row-1, "col": col, "from": "bottom"}
    elif bottom_char in ["|", "L", "J"]:
        next_char = {"row": row+1, "col": col, "from": "top"}
    elif left_char in ["-", "L", "F"]:
        next_char = {"row": row, "col": col-1, "from": "right"}
    elif right_char in ["-", "7", "J"]:
        next_char = {"row": row, "col": col+1, "from": "left"}

    steps = 0

    while lines[next_char["row"]][next_char["col"]] != "S":
        steps += 1
        char = lines[next_char["row"]][next_char["col"]]
        if char == "|":
            if next_char["from"] == "bottom":
                next_char = {"row": next_char["row"]-1, "col": next_char["col"], "from": "bottom"}
            if next_char["from"] == "top":
                next_char = {"row": next_char["row"]+1, "col": next_char["col"], "from": "top"}
        elif char == "-":
            if next_char["from"] == "left":
                next_char = {"row": next_char["row"], "col": next_char["col"]+1, "from": "left"}
            if next_char["from"] == "right":
                next_char = {"row": next_char["row"], "col": next_char["col"]-1, "from": "right"}
        elif char == "F":
            if next_char["from"] == "bottom":
                next_char = {"row": next_char["row"], "col": next_char["col"]+1, "from": "left"}
            if next_char["from"] == "right":
                next_char = {"row": next_char["row"]+1, "col": next_char["col"], "from": "top"}
        elif char == "L":
            if next_char["from"] == "top":
                next_char = {"row": next_char["row"], "col": next_char["col"]+1, "from": "left"}
            if next_char["from"] == "right":
                next_char = {"row": next_char["row"]-1, "col": next_char["col"], "from": "bottom"}
        elif char == "J":
            if next_char["from"] == "top":
                next_char = {"row": next_char["row"], "col": next_char["col"]-1, "from": "right"}
            if next_char["from"] == "left":
                next_char = {"row": next_char["row"]-1, "col": next_char["col"], "from": "bottom"}
        elif char == "7":
            if next_char["from"] == "bottom":
                next_char = {"row": next_char["row"], "col": next_char["col"]-1, "from": "right"}
            if next_char["from"] == "left":
                next_char = {"row": next_char["row"]+1, "col": next_char["col"], "from": "top"}

    return (steps + 1) / 2


# Check Solution
util.check_solution(solution, test_data, test_result, util.one_case)

# Execute Solution
result = util.run_solution(solution, util.one_case)

print("Result: " + str(result))
