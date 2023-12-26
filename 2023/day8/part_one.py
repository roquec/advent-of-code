import math

import regex as re
from shared import util, matrix

"""
    2023 Day 8: Haunted Wasteland
    https://adventofcode.com/2023/day/8
"""

# Example Data
test_data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

# Example Result
test_result = 6


# Solution
def solution(data):
    lines = data.split('\n')

    instructions = lines[0]

    nodes = {}

    for node_line in lines[2:]:
        parts = node_line.split(" = ")
        node = parts[0]
        links = parts[1].replace("(", "").replace(")", "").split(", ")
        nodes[node] = {"left": links[0],  "right": links[1]}

    current_node = "AAA"
    target_node = "ZZZ"
    current_step = 0
    total_steps = 0

    while current_node != target_node:
        total_steps += 1
        if current_step == len(instructions):
            current_step = 0
        step = instructions[current_step]
        if step == "L":
            current_node = nodes[current_node]["left"]
        else:
            current_node = nodes[current_node]["right"]
        current_step += 1

    return total_steps


# Check Solution
util.check_solution(solution, test_data, test_result, util.one_case)

# Execute Solution
result = util.run_solution(solution, util.one_case)

print("Result: " + str(result))
