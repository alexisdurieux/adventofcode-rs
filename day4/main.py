from collections import defaultdict, Counter
from typing import Dict, List, Tuple

if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
    numbers = list(map(int, lines[0].split(",")))
    current_grid = -1
    numbers_dict: Dict[int, Dict[int, List[Tuple[int, int]]]] = defaultdict(lambda: defaultdict(list))
    grids: List[List[int]] = []
    row = 0
    for line in lines[1:]:
        if line == "\n":
            current_grid += 1
            grids.append([])
            row = 0
            continue
        grids[current_grid].append(list((map(int, filter(lambda s: s != "", line.strip().split(" "))))))
        for idx, el in enumerate(map(int, filter(lambda s: s != "", line.strip().split(" ")))):
            numbers_dict[el][current_grid].append((row, idx))
        row += 1

    def get_grid(part_1: bool = False):
        won = set()
        winner_grid, winner_number = None, None
        for n in numbers:
            for grid in numbers_dict[n]:
                if grid in won:
                    continue
                for row, col in numbers_dict[n][grid]:
                    grids[grid][row][col] = 0
                    is_bingo = True
                    for i in range(5):
                        if grids[grid][i][col] != 0:
                            is_bingo = False
                    if is_bingo: 
                        won.add(grid)
                        if part_1:
                            return grids[grid], n
                        winner_grid, winner_number = grids[grid], n
                    is_bingo = True
                    for i in range(5):
                        if grids[grid][row][i] != 0:
                            is_bingo = False
                    if is_bingo: 
                        won.add(grid)
                        if part_1:
                            return grids[grid], n
                        winner_grid, winner_number = grids[grid], n
        return winner_grid, winner_number
    winning_grid, number = get_grid(True)
    
    print(number, winning_grid)
    s = 0
    for row in winning_grid:
        for el in row:
            s += el
    
    print(s * number)
    
    winning_grid, number = get_grid()
    
    print(number, winning_grid)
    s = 0
    for row in winning_grid:
        for el in row:
            s += el
    
    print(s * number)
    #print(grids)