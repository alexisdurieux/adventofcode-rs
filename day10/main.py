from queue import LifoQueue
from typing import List, Optional


ERROR_SYNTAX_VALUE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

COMPLETE_VALUE = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

OPEN_CHARS = { "(", "[", "{", "<" }
CLOSE_CHARS = { ")", "]", "}", ">" } 

SYNTAX_MAPPING = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

def solve_part1(lines: List[str]) -> int:
    def solve_line(line: str) -> int:
        queue: LifoQueue[str] = LifoQueue()
        for char in line:
            if char in OPEN_CHARS:
                queue.put(char)
            elif char in CLOSE_CHARS:
                if queue.empty():
                    return ERROR_SYNTAX_VALUE[char]
                if SYNTAX_MAPPING[char] != queue.get():
                    return ERROR_SYNTAX_VALUE[char]
        return 0
    return sum([solve_line(line) for line in lines])

def solve_part2(lines: List[str]) -> int:
    def solve_line(line: str) -> Optional[int]:
        queue: LifoQueue[str] = LifoQueue()
        for char in line:
            if char in OPEN_CHARS:
                queue.put(char)
            elif char in CLOSE_CHARS:
                if queue.empty():
                    return None
                if SYNTAX_MAPPING[char] != queue.get():
                    return None
        res = 0
        while not queue.empty():
            res *= 5
            res += COMPLETE_VALUE[queue.get()]
        return res
    results: List[int] = list(filter(lambda e: e is not None, [solve_line(line) for line in lines])) # type: ignore
    return sorted(results)[len(results) // 2]



if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('input.txt')]
    res1 = solve_part1(lines)
    print(res1)

    res2 = solve_part2(lines)
    print(res2)