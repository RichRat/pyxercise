import time


def timed_run(foo):
    start_time = time.time()
    foo()

    runtime = time.time() - start_time



    second = 1
    minute = second * 60
    hour = minute * 60
    out = []
    def t_append(span, char):
        out.append(str(int(runtime / span))  + char)
        return runtime % span

    if runtime > hour:
        runtime = t_append(hour, " h")
    if runtime > minute:
        runtime = t_append(minute, " m")
    if runtime > second:
        runtime = t_append(second, " s")
    if runtime > 0:
        out.append(str(runtime * 1000)[:6] + " ms")

    print("------ " + " ".join(out) + " ------")