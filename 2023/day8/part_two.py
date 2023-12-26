import math

import regex as re
from shared import util, matrix

"""
    2023 Day 8: Haunted Wasteland
    https://adventofcode.com/2023/day/8
"""

# Example Data
test_data = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

# Example Result
test_result = 6


# Solution
def solution(data):
    lines = data.split('\n')

    instructions = lines[0]

    nodes = {}
    current_nodes = []

    for node_line in lines[2:]:
        parts = node_line.split(" = ")
        node = parts[0]
        links = parts[1].replace("(", "").replace(")", "").split(", ")
        nodes[node] = {"left": links[0],  "right": links[1]}
        if node[-1] == "A":
            current_nodes.append(node)

    is_done = False
    current_step = 0
    total_steps = 0

    current_nodes = [current_nodes[0]]

    while not is_done:
        print(current_nodes)
        total_steps += 1
        if current_step == len(instructions):
            current_step = 0
        step = instructions[current_step]
        new_nodes = []
        is_done = True
        for current_node in current_nodes:
            if step == "L":
                new_node = nodes[current_node]["left"]
            else:
                new_node = nodes[current_node]["right"]
            new_nodes.append(new_node)
            if new_node[-1] != "Z":
                is_done = False
        current_nodes = new_nodes
        current_step += 1

    return total_steps


# Check Solution
# util.check_solution(solution, test_data, test_result, util.one_case)

# Execute Solution
result = util.run_solution(solution, util.one_case)

print("Result: " + str(result))
