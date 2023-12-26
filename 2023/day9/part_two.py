from shared import util, matrix

"""
    2023 Day 9: Mirage Maintenance
    https://adventofcode.com/2023/day/9
"""

# Example Data
test_data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

# Example Result
test_result = 2


def solve_sequence(sequence):
    result_sequence = []
    for index, number in enumerate(sequence):
        if index > 0:
            result_sequence.append(int(sequence[index]) - int(sequence[index - 1]))
    return result_sequence


# Solution
def solution(data):
    sequence = data.split(" ")

    first_elements = []

    while not all(int(element) == 0 for element in sequence):
        first_elements.append(int(sequence[0]))
        sequence = solve_sequence(sequence)

    first_elements = first_elements[::-1]

    element = 0

    for first_element in first_elements:
        element = first_element - element

    return element


# Check Solution
util.check_solution(solution, test_data, test_result)

# Execute Solution
result = util.run_solution(solution)

print("Result: " + str(result))
