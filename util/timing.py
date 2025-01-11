import time


def timed_run(foo):
    sw = Stopwatch()
    foo()
    sw.stop_print()


class Stopwatch:

    def __init__(self):
        self.start_time = time.time()
        self.run_time = 0

    def stop_print(self, reset=False):
        self.run_time = runtime = time.time() - self.start_time
        self.print()

        if reset:
            self.start_time = time.time()

    def print(self):
        print("------ " + str(self) + " ------")

    def __str__(self):
        if self.run_time == 0:
            return "no time"

        second = 1
        minute = second * 60
        hour = minute * 60
        out = []

        def t_append(span, char):
            out.append(str(int(rt / span)) + char)
            return rt % span

        rt = self.run_time
        if rt > hour:
            rt = t_append(hour, " h")
        if rt > minute:
            rt = t_append(minute, " m")
        if rt > second:
            rt = t_append(second, " s")
        if rt > 0:
            out.append(str(rt * 1000)[:6] + " ms")

        return " ".join(out)





