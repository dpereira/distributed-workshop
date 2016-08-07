import sys
import threading
import time


class Counter:
    counter = 0
    running = False

    def __init__(self):
        self.start()

    def _throuput_counter(self):
        while self.running:
            print "\r{} requets/s".format(self.counter),
            sys.stdout.flush()
            self.counter = 0
            time.sleep(1)

    def start(self):
        self.thread = threading.Thread(
            target=self._throuput_counter
        )

        self.running = True

        self.thread.start()

    def stop(self):
        self.running = False
        self.join()

    def join(self):
        self.thread.join()

    def inc(self):
        self.counter += 1
