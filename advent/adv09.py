from util.math_util import reversed_en
from util.timing import timed_run


def advent_09():
    with open('../resources/advent/9_input.txt') as list_file:
       def_line = [ int(c) for c in list_file.read()]

    drive = []
    index = []
    for i in range(len(def_line)):
        s = i // 2 if i % 2 == 0 else -1
        drive.extend([s] * def_line[i])


    def get_span(fid, start_at, delta):
        offset = delta
        while drive[start_at + offset] == fid:
            offset += delta

        end_at = start_at + (offset - delta)
        return min(start_at, end_at), max(start_at, end_at)

    def get_span_len(start, end):
        return end - start + 1

    def write_to_drive(start, len, content):
        for i in range(start, start + len):
            drive[i] = content

    skip = {-1}
    for i, fid in reversed_en(drive):
        if fid not in skip:
            span = get_span(fid, i, -1)
            span_len = get_span_len(*span)
            for j in range(len(drive)):
                if j >= i: break
                if drive[j] != -1: continue

                free_span = get_span(-1, j, 1)
                if get_span_len(*free_span) >= span_len:
                    write_to_drive(free_span[0], span_len, fid)
                    write_to_drive(span[0], span_len, -1)
                    moved = True
                    break

            skip.add(fid)


    result = sum([ i * v if v > 0 else 0 for i, v in enumerate(drive) ])
    #print("".join([ '.' if v < 0 else str(v) for v in drive ]))
    print("result " + str(result))


timed_run(advent_09)