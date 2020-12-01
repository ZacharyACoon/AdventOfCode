import time


intervals = {
    60*60*24*365: "years",
    60*60*24: "days",
    60*60: "hours",
    60: "minutes",
    -float('inf'): "seconds"
}


def human_time_interval(n):
    for i, v in intervals.items():
        if n > i:
            return f"{n/i:.2f} {v}"


class Timer:
    def __init__(self, report_interval=3):
        self.start = None
        self.stop = None
        self.interval = None
        self.clicks = []
        self.report_interval = report_interval
        self.last_report = time.time()

    def __enter__(self):
        self.start = self.last = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time()
        self.interval = self.stop - self.start

    def __repr__(self):
        return f"{self.clicks}"

    def click(self):
        self.clicks.append(time.time())

    def slope(self):
        l = len(self.clicks)
        if l == 1:
            return 0

        x1 = 0
        y1 = self.clicks[x1]
        x2 = l - 1
        y2 = self.clicks[x2]
        return (y2 - y1) / (x2 - x1)

    def eta(self, n):
        y = n * self.slope()
        return human_time_interval(y)

    def time_for_report(self):
        t = time.time()
        time_since = t - self.last_report
        if time_since > self.report_interval:
            self.last_report = t
            return True
