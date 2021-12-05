from collections import Counter
from dataclasses import dataclass
from typing import List, Set, Tuple

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Line:
    start: Point
    end: Point


def str_to_point(s: str) -> Point:
    spl = s.strip().split(',')
    return Point(int(spl[0]), int(spl[1]))

def load(filename: str) -> List[Line]:
    lines: List[Line] = []
    max_x, max_y = 0, 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            [start, end] = list(map(str_to_point, line.split('->')))
            max_x = max(max_x, max(start.x, end.x))
            max_y = max(max_y, max(start.y, end.y))
            lines.append(
                Line(
                    start=start,
                    end=end
                )
            )
    return lines

def get_step(a: int, b: int) -> int:
    if a < b: 
        return 1
    if a > b: 
        return -1
    return 0

def solve(lines: List[Line], part1: bool) -> int:
    board: Counter[Tuple[int, int]] = Counter()
    results: Set[Tuple[int, int]] = set()
    for l in lines:
        if part1 and l.start.x != l.end.x and l.start.y != l.end.y:
            continue
        step_x = get_step(l.start.x, l.end.x)
        step_y = get_step(l.start.y, l.end.y)
        i, j = l.start.x, l.start.y
        while i != l.end.x + step_x or j != l.end.y + step_y:
            board[(i, j)] += 1
            if i == l.end.x: step_x = 0
            if j == l.end.y: step_y = 0
            if board[(i,j)] > 1:
                results.add((i, j))
            i += step_x
            j += step_y
            
    return len(results)

if __name__ == "__main__":
    m = load("input.txt")
    print(solve(m, True))
    print(solve(m, False))