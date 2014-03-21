from time import sleep
from datetime import datetime, timedelta
from sys import stdout


class PomodoroException(Exception):
    pass


class Pomodoro(object):

    def __init__(self, current_time=None, end_time=None, time_left=None):
        self.current_time = datetime.now()
        self.end_time = None
        self.time_left = None
        # Constants represent number of minutes.
        self.POMODORO_LENGTH = 25
        self.SHORT_BREAK = 5
        self.LONG_BREAK = 15

    def do_pomodoro(self):
        self._run_duration(number_of_minutes=self.POMODORO_LENGTH)

    def take_long_break(self):
        self._run_duration(number_of_minutes=self.LONG_BREAK)

    def take_short_break(self):
        self._run_duration(number_of_minutes=self.SHORT_BREAK)

    def _run_duration(self, number_of_minutes):
        time_duration = timedelta(minutes=number_of_minutes)
        self._update_current_time()
        self.end_time = self.current_time + time_duration
        self._countdown()

    def _countdown(self):
        self._update_time_left()
        while self._any_time_left():
            self._print_time_left()
            self._alert_end_of_period()

    def _print_time_left(self):
        if self._any_time_left():
            stdout.write("\r" + str(self.time_left))
            stdout.flush()

    def _alert_end_of_period(self):
        self._update_times()
        if not self._any_time_left():
            # Play a sound file here.
            print("\n\aDone!")
        else:
            sleep(1)

    def _any_time_left(self):
        return self.time_left.days >= 0

    def _update_times(self, end_time=None):
        self._update_current_time()
        self._update_time_left()

    def _update_current_time(self):
        self.current_time = datetime.now()

    def _calculate_time_left(self):
        self.time_left = self.end_time - self.current_time

    def _update_time_left(self, end_time=None):
        if self.end_time:
            self._calculate_time_left()
        elif end_time:
            self.time_left = end_time - self.current_time
        else:
            raise PomodoroException("end_time was not specified.")

    @property
    def get_times(self):
        return {
            'current_time':  self.current_time,
            'end_time':      self.end_time,
            'time_left':     self.time_left
        }
