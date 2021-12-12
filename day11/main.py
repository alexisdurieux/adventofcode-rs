from os import error
import numpy as np
from typing import Tuple
from functools import reduce

def load(filename: str):
    with open(filename) as f:
        l = []
        for line in f:
            l.append([int(c) for c in line.strip()])
        return np.array(l)

def solve_part_1(data: np.ndarray) -> int:
    def explode_neighbours(a: np.array, x: int, y: int) -> np.array:
        # import pdb; pdb.set_trace()
        if x - 1 >= 0:
            if a[x - 1, y] != 0:
                a[x - 1, y] += 1
        if x + 1 < a.shape[0]:
            if a[x + 1, y] != 0:
                a[x + 1, y] += 1
        if y - 1 >= 0:
            if a[x, y - 1] != 0:
                a[x, y - 1] += 1
        if y + 1 < a.shape[1]:
            if a[x, y + 1] != 0:
                a[x][y + 1] += 1
        if x - 1 >= 0 and y - 1 >= 0:
            if a[x - 1, y - 1] != 0:
                a[x - 1, y - 1] += 1
        if x + 1 < a.shape[0] and y - 1 >= 0:
            if a[x + 1, y - 1] != 0:
                a[x + 1, y - 1] += 1
        if x - 1 >= 0 and y + 1 < a.shape[1]:
            if a[x - 1, y + 1] != 0:
                a[x - 1, y + 1] += 1
        if x + 1 < a.shape[0] and y + 1 < a.shape[1]:
            if a[x + 1, y + 1] != 0:
                a[x + 1, y + 1] += 1
        a[x, y] = 0
        return a

    def step(previous_explosions: int, arr: np.ndarray) -> Tuple[int, np.ndarray]:
        explosions: int = 0
        arr = arr + 1
        while np.sum(arr > 9) > 0:
            # import pdb; pdb.set_trace()
            for i in range(arr.shape[0]):
                for j in range(arr.shape[1]):
                    # import pdb; pdb.set_trace()
                    if arr[i, j] > 9:
                        explosions += 1
                        arr = explode_neighbours(arr, i, j)
        return (explosions + previous_explosions, arr)
    acc = 0
    for i in range(100):
        acc, data = step(acc, data)
        print(data)
        # import pdb; pdb.set_trace()
    return acc

def solve_part_2(data: np.ndarray) -> int:
    def explode_neighbours(a: np.array, x: int, y: int) -> np.array:
        # import pdb; pdb.set_trace()
        if x - 1 >= 0:
            if a[x - 1, y] != 0:
                a[x - 1, y] += 1
        if x + 1 < a.shape[0]:
            if a[x + 1, y] != 0:
                a[x + 1, y] += 1
        if y - 1 >= 0:
            if a[x, y - 1] != 0:
                a[x, y - 1] += 1
        if y + 1 < a.shape[1]:
            if a[x, y + 1] != 0:
                a[x][y + 1] += 1
        if x - 1 >= 0 and y - 1 >= 0:
            if a[x - 1, y - 1] != 0:
                a[x - 1, y - 1] += 1
        if x + 1 < a.shape[0] and y - 1 >= 0:
            if a[x + 1, y - 1] != 0:
                a[x + 1, y - 1] += 1
        if x - 1 >= 0 and y + 1 < a.shape[1]:
            if a[x - 1, y + 1] != 0:
                a[x - 1, y + 1] += 1
        if x + 1 < a.shape[0] and y + 1 < a.shape[1]:
            if a[x + 1, y + 1] != 0:
                a[x + 1, y + 1] += 1
        a[x, y] = 0
        return a

    def step(previous_explosions: int, arr: np.ndarray) -> Tuple[int, np.ndarray]:
        explosions: int = 0
        arr = arr + 1
        while np.sum(arr > 9) > 0:
            # import pdb; pdb.set_trace()
            for i in range(arr.shape[0]):
                for j in range(arr.shape[1]):
                    # import pdb; pdb.set_trace()
                    if arr[i, j] > 9:
                        explosions += 1
                        arr = explode_neighbours(arr, i, j)
        return (explosions + previous_explosions, arr)
    acc = 0
    i = 0
    while np.sum(data == 0) != 100:
        acc, data = step(acc, data)
        i += 1
    return i



if __name__ == '__main__':
    arr = load('input_test.txt')
    print(solve_part_1(arr))
    print(solve_part_2(arr))