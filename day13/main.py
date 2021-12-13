import numpy as np
from PIL import Image

def load(filename: str) -> np.array:
    with open(filename, 'r') as f:
        points = []
        lines = f.readlines()
        instructions = []
        for idx, line in enumerate(lines):
            if line == "\n":
                break
            points.append(tuple(map(int, line.split(','))))
        for line in lines[idx+1:]:
            [axis, value] = line.split(" ")[-1].split("=")
            instructions.append((axis, int(value)))
        return points, instructions

if __name__ == "__main__":
    points, instructions = load("input.txt")
    max_x, max_y = max(points, key=lambda x: x[0])[0], max(points, key=lambda x: x[1])[1]
    grid = np.full((max_y + 1, max_x + 1), False)
    for point in points:
        grid[point[1], point[0]] = True
    for instruction in instructions[0:1]:
        print(instruction)
        if instruction[0] == "x":
            grid = np.logical_or(np.fliplr(grid[:, instruction[1] + 1:]), grid[:, :instruction[1]]).astype(int)
        elif instruction[0] == "y":
            grid = np.logical_or(np.flipud(grid.astype(int)[instruction[1] + 1:, :]),grid.astype(int)[:instruction[1], :]).astype(int)
    print(np.sum(grid))
    for instruction in instructions[1:]:
        print(instruction)
        if instruction[0] == "x":
            grid = np.logical_or(np.fliplr(grid[:, instruction[1] + 1:]), grid[:, :instruction[1]]).astype(int)
        elif instruction[0] == "y":
            grid = np.logical_or(np.flipud(grid.astype(int)[instruction[1] + 1:, :]),grid.astype(int)[:instruction[1], :]).astype(int)
    Image.fromarray(grid.astype('uint8')*255).show()
    print(np.sum(grid))
    
        
