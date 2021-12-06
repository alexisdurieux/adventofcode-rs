from collections import Counter
from typing import Counter, Dict, List
import time

def load(filename: str):
    with open(filename) as f:
        line = f.readlines()[0]
        return [int(char) for char in line.split(",")]
    
def run_simulation(days: int, fishes: List[int]) -> List[int]:
    def run_day(l: List[int]) -> List[int]:
        to_append = 0
        for idx, f in enumerate(l):
            if f == 0:
                l[idx] = 6
                to_append += 1
            else:
                l[idx] -= 1
        # print(l + [8] * to_append)
        return l + [8] * to_append

                
    if days == 0:
        return fishes
    else:
        return run_simulation(days - 1, run_day(fishes))

def with_dict(days: int, fishes: List[int]) -> int:
    d: Dict[int, int] = { i: 0 for i in range(-1, 9) }
    for f in fishes:
        d[f] += 1
    while days > 0:
        #print("\t", d)
        for i in range(0, 9):
            d[i - 1] = d[i]
        d[8] = d[-1]
        d[6] += d[-1]
        days -= 1
    return sum(d.values()) - d[-1]

if __name__ == '__main__':
    fishes = load("input.txt")
    tic = time.perf_counter()
    res_80 = with_dict(80, fishes)
    toc = time.perf_counter()
    print(f"Part 1: {res_80} in {toc - tic} seconds")

    tic = time.perf_counter()
    res_256 = with_dict(256, fishes)
    toc = time.perf_counter()
    print(f"Part 2: {res_256} in {toc - tic} seconds")
