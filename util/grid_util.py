from util.vector import IntVector2



def grid_coords(grid: list[list]):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            yield IntVector2(x, y)