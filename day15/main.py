import numpy as np
from typing import Tuple, Set, List
import time
import heapq

Coordinates = Tuple[int, int]

def load(filename: str) -> np.ndarray:
    with open(filename) as f:
        l = []
        for line in f:
            l.append([int(c) for c in line.strip()])
        return np.array(l)

def solve2(a: np.ndarray, tiles: int = 1) -> int:
    def get_neighbours(s: Coordinates, p: Coordinates) -> Set[Coordinates]:
        x, y = p
        neighbours: Set[Coordinates] = set()
        if x - 1 >= 0:
            neighbours.add((x - 1, y))
        if x + 1 < a.shape[0] * tiles:
            neighbours.add((x + 1, y))
        if y - 1 >= 0:
            neighbours.add((x, y - 1))
        if y + 1 < a.shape[1] * tiles:
            neighbours.add((x, y + 1))
        return neighbours

    start = (0, 0)
    distances = np.full((a.shape[0]*tiles, a.shape[1]*tiles), np.inf)
    candidates: List[Tuple[int, Coordinates]] = [(0, start)]
    while candidates:
        (dist, p) = heapq.heappop(candidates)
        val = a[(p[0]%a.shape[0], p[1]%a.shape[1])] + (p[0]//a.shape[0]) + (p[1]//a.shape[1])
        while val > 9:
            val -= 9
        if val + dist < distances[p]:
            distances[p] = val + dist
            if p == (a.shape[0] * tiles - 1, a.shape[1] * tiles - 1):
                break
            neighbours = get_neighbours(a, p)
            for n in neighbours:
                heapq.heappush(candidates, (distances[p], n))
    return distances[a.shape[0] * tiles - 1, a.shape[1] * tiles - 1] - distances[(0, 0)]

if __name__ == '__main__':
    arr = load("input.txt")
    print(solve2(arr))
    print(solve2(arr, tiles=5))
    