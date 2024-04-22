'''

Timer Utils

Created By: Richard Schmidt
Github: ScRichard
Last update: 20.4. 2024

'''

import time

class Timer:
    def __init__(self):
        self.startTime = -1
    def has_ellapsed(self, millis : int, repeat : bool):
        if self.startTime == -1:
            self.reset()

        if time.time()*1000-self.startTime >= millis:
            if repeat:
                self.reset()
            return True
        return False
    def reset(self):
        self.startTime = time.time() * 1000