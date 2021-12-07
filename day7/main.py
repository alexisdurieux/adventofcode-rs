from functools import cache
from typing import List, Dict

def load(filename: str) -> List[int]:
    with open(filename) as f:
        line = f.readlines()[0]
        return [int(x) for x in line.split(',')]

@cache
def compute_consumption(distance: int):
    if distance == 0:
        return 0
    v = sum([i + 1 for i in range(distance)])
    return v

def solve(l: List[int], part1: bool) -> int:
    consumptions = [0] * max(l)
    for e in l:
        for i in range(len(consumptions)):
            consumptions[i] += abs(e-i) if part1 else compute_consumption(abs(e - i))
    return min(consumptions)



if __name__ == "__main__":
    crabs = load('input.txt')
    print(solve(crabs, True))
    print(solve(crabs, False))
    