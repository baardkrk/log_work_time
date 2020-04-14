import time

class TimerObject:
    """
    Timer Object for storing state of timer
    """
    def __init__(self):
        self.t0
        self.elapsed_time = 0.00
        self.paused = False
        self.stop_count = 0

    def start_timer():
        self.t0 = time.time()
        self.paused = False

    def pause_timer():
        self.paused = True
        self.stop_count++
        self.elapsed_time = time.time() - self.t0

    def is_paused():
        return self.paused

    def elapsed():
        if self.is_paused():
            return elapsed_time
        return elapsed_time + (time.time() - self.t0)

    def seconds():
        return self.elapsed()

    def minutes():
        return self.elapsed() / 60

    def hours():
        return self.elapsed() / 3600

    def days():
        return self.elapsed() / 86400

