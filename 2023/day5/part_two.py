import regex as re
from shared import util, matrix

"""
    2023 Day 5: If You Give A Seed A Fertilizer
    https://adventofcode.com/2023/day/5
"""

# Example Data
test_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

# Example Result
test_result = 46


# Set up

# Solution
def process_seed(seed_start, seed_end, steps):
    source_ranges = [[seed_start, seed_end]]
    destination_ranges = []

    for step in steps:
        destination_ranges = []
        for source_range in source_ranges:
            step_ranges = sorted(step, key=lambda item: item[1])

            thresholds = [source_range[0]]
            for step_range in step_ranges:
                if source_range[0] < step_range[1] < source_range[1] and not step_range[1] in thresholds:
                    thresholds.append(step_range[1])
                if source_range[0] < (step_range[1] + step_range[2]) < source_range[1] and not (step_range[1] + step_range[2]) in thresholds:
                    thresholds.append((step_range[1] + step_range[2]))
            if not source_range[1] in thresholds:
                thresholds.append(source_range[1])



        destination = -1
        for range in step:
            if range[1] <= source < (range[1] + range[2]):
                destination = range[0] + (source - range[1])
        if destination == -1:
            destination = source
        source = destination

    return destination


def solution(data):
    location = -1

    seeds = [int(item) for item in data.split('\n')[0][7:].split(' ')]
    steps = [[[int(x) for x in item.split(' ')] for item in step.split('\n')] for step in re.split(r'\n\n.+:\n', data)[1:]]

    for seed in seeds:
        if location == -1:
            location = process_seed(seed, steps)
        else:
            location = min(location, process_seed(seed, steps))

    return location


# Check Solution
util.check_solution(solution, test_data, test_result, util.one_case)

# Execute Solution
result = util.run_solution(solution, util.one_case)

print("Result: " + str(result))
