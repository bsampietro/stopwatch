import time

class Clock:
    def __init__(self):
        self.initialize_time_variables()
        self.running = False

    def start(self):
        if self.running:
            return
        self.running = True
        self._start_time = time.time()

    def stop(self):
        if not self.running:
            return
        self.running = False
        self._elapsed_time += int(time.time() - self._start_time)

    def reset(self):
        self.initialize_time_variables()
        self.running = False
        # if self.running:
        #     self.start()

    def move(self, duration):
        self._elapsed_time += duration

    def display_time(self, with_seconds):
        elapsed_time = self.elapsed_time()
        sign = '-' if elapsed_time < 0 else ''
        elapsed_time = abs(elapsed_time)
        hours = elapsed_time // 3600
        minutes = (elapsed_time - hours * 3600) // 60
        result = '%s%02d:%02d' % (sign, hours, minutes)
        if with_seconds:
            seconds = elapsed_time - (hours * 3600 + minutes * 60)
            result += ':%02d' % seconds
        return result

    # Private

    def initialize_time_variables(self):
        self._start_time = None
        self._elapsed_time = 0

    def elapsed_time(self):
        if self.running:
            return self._elapsed_time + int(time.time() - self._start_time)
        else:
            return self._elapsed_time
