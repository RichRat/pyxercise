from util.grid_util import grid_walk_val
from util.timing import timed_run
from util.vector import IntVector2 as Iv, null_vector


def advent_15_step_1():
    with open('../resources/advent/15_input.txt') as list_file:
       lines = [ line for line in list_file.read().split("\n")]

    grid = [ [ c for c in line ] for line in lines if line.startswith('#')]
    bot_pos = None
    for pos, v in grid_walk_val(grid):
        if v == '@':
            bot_pos = pos
            break

    dir_dict = {
        '^': Iv(0, -1),
        '>': Iv(1, 0),
        'v': Iv(0, 1),
        '<': Iv(-1, 0)
    }
    bot_moves = "".join([ line for line in lines if len(line) > 0 and line[0] in dir_dict ])
    def do_move(v_dir, v_pos):
        next_pos = v_pos + v_dir
        next_pos_val = next_pos.of_grid(grid)
        move = False
        match next_pos_val:
            case '#': pass
            case 'O': move, _ = do_move(v_dir, next_pos)
            case '.': move = True

        if move:
            next_pos.set_grid(grid, v_pos.of_grid(grid))
            v_pos.set_grid(grid, '.')

        return move, next_pos if move else v_pos




    for v_dir in [ dir_dict[c] for c in bot_moves ]:
        _, bot_pos = do_move(v_dir, bot_pos)

    result = 0
    for pos, val in grid_walk_val(grid):
        if val == 'O':
            result += pos.x + pos.y * 100

    print("result " + str(result))
    #10.7 ms


def advent_15_step_2():
    with open('../resources/advent/15_input.txt') as list_file:
       lines = [ line for line in list_file.read().split("\n")]

    map_map = {'#': '##', '.': '..', 'O': '[]', '@': '@.'}
    grid = [ [c for c in "".join([ map_map[sc] for sc in line ])] for line in lines if line.startswith('#') ]


    bot_pos = None
    for pos, val in grid_walk_val(grid):
        if val == '@':
            bot_pos = pos
            break


    dir_dict = {
        '^': Iv(0, -1),
        '>': Iv(1, 0),
        'v': Iv(0, 1),
        '<': Iv(-1, 0),
        '[': Iv(1, 0),
        ']': Iv(-1, 0)
    }

    bot_moves = "".join([ line for line in lines if len(line) > 0 and line[0] in dir_dict ])

    def do_move(v_pos: list, v_dir):
        next_pos = [ v + v_dir for v in v_pos ]
        move = True
        push_move = []
        for i, nex_val in enumerate([ v.of_grid(grid) for v in next_pos ]):
            if next_pos[i] in push_move:
                continue
            elif nex_val == '#':
                return False
            elif nex_val in '[]':
                push_move.append(next_pos[i])
                #vertical push also pushes other bracket of box
                if v_dir.y != 0:
                    push_move.append(next_pos[i] + dir_dict[nex_val])

        if move and push_move:
            move = do_move(push_move, v_dir)

        if move:
            for i, np in enumerate(next_pos):
                np.set_grid(grid, v_pos[i].of_grid(grid))
                v_pos[i].set_grid(grid, '.')

            return move

    for m in [ m for m in bot_moves ]:
        # pause marker for debugging
        if m == 'p':
            continue

        v_direction = dir_dict[m]
        if do_move([bot_pos], v_direction):
            bot_pos += v_direction

        # print("Move " + str(m))
        # print("\n".join([ "".join(line) for line in grid ]))
        # print('\n')

    result = 0
    for pos, val in grid_walk_val(grid):
        if val == '[':
            result += pos.x + pos.y * 100

    print("result " + str(result))


timed_run(advent_15_step_2)