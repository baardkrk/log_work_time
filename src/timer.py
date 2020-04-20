import time

class TimerObject:
    """
    Timer Object for storing state of timer
    """
    def __init__(self):
        self.t0 = 0
        self.elapsed_time = 0.00
        self.paused = True
        self.stop_count = 0

    def start(self):
        if self.is_paused():
            self.t0 = time.time()
            self.paused = False
            

    def pause(self):
        if not(self.is_paused()):
            self.paused = True
            self.stop_count += 1
            self.elapsed_time += time.time() - self.t0
            

    def is_paused(self):
        return self.paused
    

    def elapsed(self):
        if self.is_paused():
            return self.elapsed_time
        return self.elapsed_time + (time.time() - self.t0)
    

    def seconds(self):
        return self.elapsed()
    

    def minutes(self):
        return self.elapsed() / 60
    

    def hours(self):
        return self.elapsed() / 3600


    def timestring(self):
        time_unit = 'hours'
        elapsed_time = self.hours()
        if self.elapsed() < 60:
            time_unit = 'seconds'
            elapsed_time = self.elapsed()
        elif self.minutes() < 60:
            time_unit = 'minutes'
            elapsed_time = self.minutes()

        return '{:.2f} {}'.format(elapsed_time, time_unit)
    

    def friendly_state_string(self):        
        friendly_string = 'elapsed: {}\tStop count: {}\tPaused: {}'.format(
            self.timestring(), self.stop_count, self.paused)
        
        return friendly_string
