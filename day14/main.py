from collections import Counter, defaultdict
from typing import Tuple, Dict, List, Set

Pair = Tuple[str, str]

def build_index(s: str) -> Dict[Pair, Set[int]]:
    index: Dict[Pair, int] = defaultdict(list)
    for idx in range(len(s) - 1):
        index[s[idx], s[idx + 1]].append(idx + 1)
    return index

def load(filename: str) -> Tuple[List[str], Dict[Pair, Set[int]], Dict[Pair, str]]:
    with open(filename) as f:
        lines = f.readlines()
    sequence = list(lines[0].strip())
    index = build_index(sequence)
    pairs = defaultdict(str)
    for line in lines[2:]:
        [pair, insert] = line.strip().split(" -> ")
        pairs[(pair[0], pair[1])] = insert

    return sequence, index, pairs


def solve_part_1(sequence: str, index: Dict[Pair, Set[int]], pairs: Dict[Pair, str], steps: int = 10) -> int:
    def insert(s: str, i: int, c: str) -> str:
        return s[:i] + [c] + s[i:]
    for i in range(steps):
        insertions = set(index.keys()).intersection(set(pairs.keys()))
        offset = 0
        to_insert = defaultdict(Pair)
        for pair in insertions:
            for i in index[pair]:
                to_insert[i] = pair
        for i in sorted(to_insert.keys()):
            pair = to_insert[i]
            sequence = insert(sequence, i + offset, pairs[pair])
            offset += 1
        index = build_index(sequence)
    
    most_commons = Counter(sequence).most_common()
    return most_commons[0][1] - most_commons[-1][1]

if __name__ == "__main__":
    sequence, index, insertion_pairs = load("input.txt")

    res = solve_part_1(sequence, index, insertion_pairs, 40)
    print(res)
