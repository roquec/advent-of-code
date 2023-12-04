def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def one_case(raw_input):
    return [raw_input]


def split_by_line(raw_input):
    lines = raw_input.split('\n')
    return lines


def check_solution(solution_function, sample_input, expected_result, cases_function=split_by_line):
    cases = cases_function(sample_input)
    result = 0

    for case in cases:
        result += solution_function(case)

    if result == expected_result:
        print(f"✅ Test scenario passes: expected {expected_result} and got {result}")
    else:
        print(f"❌ Failed test scenario: expected {expected_result} and got {result}")


def run_solution(solution_function, cases_function=split_by_line, input_file="input"):
    raw_input = read_file(input_file)
    cases = cases_function(raw_input)
    result = 0

    for case in cases:
        result += solution_function(case)

    return result
