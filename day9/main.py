import numpy as np

def load(filename: str) -> np.ndarray:
    with open(filename) as f:
        res = []
        for line in f:
            res.append([int(c) for c in line.strip()])
        arr = np.full((len(res) + 2, len(res[0]) + 2), 11, dtype=np.int)
        for i in range(len(res)):
            for j in range(len(res[0])):
                arr[i + 1][j + 1] = res[i][j]
        return arr

def visit_point(arr: np.ndarray, from_value: int, i: int, j: int, visited_arr: np.ndarray) -> int:
    if visited_arr[i][j]:
        return 0
    if arr[i][j] >= 9:
        return 0
    visited_arr[i][j] = True
    return (
        1 + 
        visit_point(arr, arr[i][j], i - 1, j, visited_arr) + 
        visit_point(arr, arr[i][j], i + 1, j, visited_arr) + 
        visit_point(arr, arr[i][j], i, j - 1, visited_arr) + 
        visit_point(arr, arr[i][j], i, j + 1, visited_arr)
    )
    
def solve_part_2(arr: np.ndarray) -> int:
    bassins_sizes = []
    visited_arr = np.full(arr.shape, False, dtype=bool)
    for i in range(1, arr.shape[0] - 1):
        for j in range(1,arr.shape[1] - 1):
            if not visited_arr[i][j]:
                bassins_sizes.append(visit_point(arr, arr[i][j], i, j, visited_arr))
                # print("Next bassin")
    res = 1
    for size in sorted(bassins_sizes)[-3:]:
        res *= size
    print(sorted(bassins_sizes)[-3:])                                     
    return res

    

if __name__ == '__main__':
    arr: np.ndarray = load('input.txt')
    count = 0
    print(arr)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i, j] < arr[i - 1, j] and arr[i, j] < arr[i, j -1] and arr[i, j] < arr[i +1, j] and arr[i, j] < arr[i, j +1]: 
                count += (arr[i, j] + 1)
    print(count)
    print(solve_part_2(arr))
    
    