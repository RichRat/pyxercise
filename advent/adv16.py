from util.grid_util import grid_walk_val
from util.timing import timed_run
from util.vector import IntVector2 as Iv, null_vector


def advent_16_step_1():
    with open('../resources/advent/16_input.txt') as list_file:
       maze = [ [ c for c in line ] for line in list_file.read().split("\n")]

    dirs = [ Iv(1,0), Iv(0, 1), Iv(-1, 0), Iv(0, -1) ]

    #print("result " + str(result))
    start_pos = Iv(1, len(maze) - 2)
    start_dir = 0

    results = []
    min_result = [10**20]


    def run_maze(pos, dir, trail, score=0):
        if pos.of_grid(maze) == "E":
            if score < min_result[0]:
                min_result[0] = score
                results.append((score, trail))
            return

        dl = None
        while True:
            dl = [ (i + dir) % len(dirs) for i in range(-1,2) ]
            dl = [ d for d in dl if (pos + dirs[d]).of_grid(maze) != "#" and (pos + dirs[d]).of_grid(maze) not in trail]
            if len(dl) == 0:
                return
            if len(dl) == 1:
                nex_dir = dirs[dl[0]]
                nex_val = (pos + dirs[dl[0]]).of_grid(maze)
                if nex_val == "E":
                    run_maze(pos, nex_dir, trail, score)
                else:
                    score += 1 if dir == nex_dir else 1001
                    pos = pos + dirs[nex_dir]

            if len(dl) > 1:
                break

        for d in dl:
            new_dir = dirs[d]
            new_pos = pos + new_dir
            if new_pos.of_grid(maze) != "#" and new_pos not in trail:
                step_score = 1 if d == dir else 1001
                run_maze(new_pos, d, trail + [new_pos], score + step_score)




    run_maze(start_pos, start_dir, [start_pos])

    dir_str = ['>', 'v', '<', '^']
    for score, path in results:
        print("score " + str(score))
        s_lines = [ [ c for c in line ] for line in maze ]
        for i, pos in enumerate(path):
            if i + 1 != len(path):
                s_lines[pos.y][pos.x] = dir_str[dirs.index(path[i+1] - pos)]

        print("\n".join([ "".join(line) for line in s_lines ]))

        print('\n')
    #print("result " + str(result))


timed_run(advent_16_step_1)