from util.vector import IntVector2



def grid_walk(grid: list[list]):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            yield IntVector2(x, y)

def grid_walk_val(grid: list[list]):
    for pos in grid_walk(grid):
        yield pos, pos.of_grid(grid)


orientations = [
    IntVector2(1, 0),
    IntVector2(1, 1),
    IntVector2(0, 1),
    IntVector2(-1, 1),
    IntVector2(-1, 0),
    IntVector2(-1, -1),
    IntVector2(0, -1),
    IntVector2(1, -1),
]

def grid_neighbors(pos: IntVector2, grid: list[list]):
    for d in orientations:
        new_pos = d + pos
        if new_pos.is_in_bounds(grid):
            yield new_pos, new_pos.of_grid(grid)
