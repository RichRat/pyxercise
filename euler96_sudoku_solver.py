# euler 96 sudoku
import time
from typing import Self

verbose_grid = True


class Pentry:

    def __init__(self, x, y, possible_values):
        self.x = x
        self.y = y
        self.ps = possible_values

    def __len__(self):
        return len(self.ps)

    def __str__(self):
        return 'PEntry (' + str(self.x) + ", " + str(self.y) + ") ps: " + str(self.ps)


class Action:

    def __init__(self, p: Pentry, parent: Self):
        self.parent = parent
        self.x = p.x
        self.y = p.y
        self.options = p.ps
        self.optInd = 0

    def do(self, content):
        content[self.y][self.x] = self.options[self.optInd]
        #print('set' + ('opt ' + str(self.optInd) if self.is_option() else "") + ' (' + str(self.x) + ", " + str(self.y) + ") n: " + str(self.options[self.optInd]))
        return self

    def undo(self, content):
        content[self.y][self.x] = 0
        #print('undo (' + str(self.x) + ", " + str(self.y) + ") n: 0")
        return self

    def is_option(self):
        return self.optInd + 1 < len(self.options) > 1

    def trace_back_and_try_option(self, content):
        self.undo(content)
        if self.is_option():
            self.optInd += 1
            return self.do(content)
        elif self.parent is not None:
            return self.parent.trace_back_and_try_option(content)
        else:
            raise Exception('no further branch Exception')


class Grid:

    def __init__(self, name):
        self.name = name
        self.content = []
        self.last_action = None

    def append_row(self, row):
        arr = [int(char) for char in row]
        self.content.append(arr)

    def solve(self):
        print('solving ' + self.name)
        self.print_grid()
        while not self.is_solved():
            if not self.solve_step():
                self.last_action = self.last_action.trace_back_and_try_option(self.content)

    def solve_step(self):
        p_space = self.gen_points()
        p_min = 11
        do_arr = []
        # get the points with the least options
        for p in p_space:
            self.reduce_p(p)
            if len(p) == 0:
                return False
            elif len(p) == p_min:
                    do_arr.append(p)
            elif len(p) < p_min:
                do_arr = [p]
                p_min = len(p)

        # set the values with the least options or one point with more than one action
        prev_act = self.last_action
        for p in do_arr:
            self.last_action = Action(p, self.last_action).do(self.content)
            if len(p) > 1:
                break

        return True

    def is_solved(self):
        return len([n + 1 for row in self.content for n in row if n == 0]) == 0
        #return len(self.gen_possibility_space()) > 0

    def gen_points(self):
        p_space = []
        for y, row in enumerate(self.content):
            for x, cell in enumerate(row):
                if cell == 0:
                    p_space.append(Pentry(x, y, [n for n in range(1, 10)]))

        return p_space

    def reduce_p(self, p):
        rem = self.get_square(p) + self.get_row(p) + self.get_column(p)
        p.ps = [n for n in p.ps if n not in rem]

    def get_square(self, p):
        x_offset = p.x - (p.x % 3)
        y_offset = p.y - (p.y % 3)
        arr = []
        for xi in range(3):
            for yi in range(3):
                cell = self.content[y_offset + yi][x_offset + xi]
                if cell > 0:
                    arr.append(cell)

        return arr

    def get_row(self, p):
        return [cell for cell in self.content[p.y] if cell > 0]

    def get_column(self, p):
        ret = []
        for row in self.content:
            if row[p.x] > 0:
                ret.append(row[p.x])

        return ret

    def print_grid(self):
        if not verbose_grid:
            return

        print('______')
        g = self.content
        for y in range(9):
            if y % 3 == 0 and 0 < y < 8:
                print('------+-------+------')

            line = ""
            for x in range(9):
                line += str(g[y][x] if g[y][x] > 0 else '.') + " "
                if x % 3 == 2 and 0 < x < 8:
                    line += '| '

            print(line)

    def get_result(self):
        top = self.content[0]
        ret = 100 * top[0] + 10 * top[1] + top[2]
        print(self.name + " result is " + str(ret))
        return ret

    def debug_verify_result(self):
        pass #TODO check all rows and squares to catch errors


start_time = time.time()
with open("resources/euler/p096_sudoku.txt") as file:
    lines = [line.rstrip() for line in file]

grids = []
grid_obj = None
for line in lines:
    if line.startswith("Grid"):
        grid_obj = Grid(line)
        grids.append(grid_obj)
    elif line.startswith("EXIT"):
        break
    else:
        grid_obj.append_row(line)

result = 0
for grid in grids:
    grid.solve()
    grid.print_grid()
    result += grid.get_result()

print('result: ' + str(result))
print("--- %s seconds ---" % (time.time() - start_time))