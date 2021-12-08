from typing import List, Dict, Set

def load(filename: str):
    with open(filename) as f:
        inputs, outputs = [], []
        for line in f:
            [input_str, output_str] = list(map(lambda s: s.strip(), line.split(' |')))
            inputs.append(input_str.split())
            outputs.append(output_str.split())
        return inputs, outputs

def format_key(s: str) -> str:
    return ''.join(sorted(s))

def solve_line(digits: List[str], output: List[str]) -> int:
    solutions: Dict[int, Set[str]] = { i: set() for i in range(len(digits))}
    inverted_index: Dict[str, str] = {}
    for digit in digits:
        if len(digit) == 2:
            solutions[1] = set(digit)
            inverted_index[format_key(digit)] = "1"
        elif len(digit) == 3:
            solutions[7] = set(digit)
            inverted_index[format_key(digit)] = "7"
        elif len(digit) == 4:
            solutions[4] = set(digit)
            inverted_index[format_key(digit)] = "4"
        elif len(digit) == 7:
            solutions[8] = set(digit)
            inverted_index[format_key(digit)] = "8"
    candidates069 = list(filter(lambda s: len(s) == 6, digits))
    for candidate in candidates069:
        count_subset = 0
        for superset in [solutions[1], solutions[7], solutions[4]]:
            count_subset += int(superset <= set(candidate))
        if count_subset == 0:
            solutions[6] = set(candidate)
            inverted_index[format_key(candidate)] = "6"
        if count_subset == 3:
            solutions[9] = set(candidate)
            inverted_index[format_key(candidate)] = "9"
        if count_subset == 2:
            solutions[0] = set(candidate)
            inverted_index[format_key(candidate)] = "0"
    candidate235 = list(filter(lambda s: len(s) == 5, digits))
    for candidate in candidate235:
        count_subset = 0
        for superset in [solutions[6], solutions[8], solutions[9]]:
            count_subset += int(set(candidate) <= superset)
        if count_subset == 3:
            solutions[5] = set(candidate)
            inverted_index[format_key(candidate)] = "5"
        if count_subset == 2:
            solutions[3] = set(candidate)
            inverted_index[format_key(candidate)] = "3"
        if count_subset == 1:
            solutions[2] = set(candidate)
            inverted_index[format_key(candidate)] = "2"
    return int("".join([inverted_index[format_key(d)] for d in output]))


def solve_part_1(inputs: List[List[str]], outputs: List[List[str]]):
    count = 0
    for output in outputs:
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                count += 1
    return count

if __name__ == '__main__':
    inputs, outputs = load('input.txt')
    part1_solution = solve_part_1(inputs, outputs)
    print(part1_solution)

    part2_solution = sum([solve_line(digits, res) for digits, res in zip(inputs, outputs)])
    print(part2_solution)
