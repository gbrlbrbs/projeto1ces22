from threading import Timer
from functools import partial


class TimerThread(object):

    def __init__(self, interval, function, args=None, kwargs=None):
        """
        Runs the function at a specified interval with given arguments.
        """
        self.interval = interval
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}
        self.function = partial(function, *args, **kwargs)
        self.running = False
        self._timer = None

    def __call__(self):
        """
        Handler function for calling the partial and continuing.
        """
        self.running = False  # mark not running
        self.start()  # reset the timer for the next go
        self.function()  # call the partial function

    def start(self):
        """
        Starts the interval and lets it run.
        """
        if self.running:
            # Don't start if we're running!
            return

            # Create the timer object, start and set state.
        self._timer = Timer(self.interval, self)
        self._timer.start()
        self.running = True

    def stop(self):
        """
        Cancel the interval (no more function calls).
        """
        if self._timer:
            self._timer.cancel()
        self.running = False
        self._timer = None
