import time

class Clock:
    def __init__(self):
        self._initialize_time_variables()
        self.running = False

    def start(self):
        if self.running:
            return
        self.running = True
        self._start_time = int(time.time())

    def stop(self):
        if not self.running:
            return
        self.running = False
        self._last_stop_time = int(time.time())
        self._elapsed_time += (int(time.time()) - self._start_time)

    def reset(self):
        self._initialize_time_variables()
        self.running = False
        # if self.running:
        #     self.start()

    def move(self, duration):
        self._elapsed_time += duration

    def elapsed_time(self):
        if self.running:
            return self._elapsed_time + (int(time.time()) - self._start_time)
        else:
            return self._elapsed_time

    def elapsed_time_since_last_stop(self):
        if self._last_stop_time:
            return int(time.time()) - self._last_stop_time
        else:
            return 0

    def _initialize_time_variables(self):
        self._start_time = None
        self._elapsed_time = 0
        self._last_stop_time = None
