#!/usr/bin/env python2
import time
import datetime
import sys


class PomodoroException(Exception):
    pass


class Pomodoro(object):

    def __init__(self, current_time=None, end_time=None, time_left=None):
        self.current_time = datetime.datetime.now()
        self.end_time = None
        self.time_left = None
        # Ints represent number of minutes.
        self.POMODORO_LENGTH = 25
        self.SHORT_BREAK = 5
        self.LONG_BREAK = 15

    def calculate_time_left(self):
        self.time_left = self.end_time - self.current_time

    def run_duration(self, number_of_minutes):
        time_duration = datetime.timedelta(minutes=number_of_minutes)
        self.end_time = self.current_time + time_duration
        self.calculate_time_left()
        while self.time_left.total_seconds() > 0:
            self.update_times()
            sys.stdout.write("\r" + str(self.end_time - self.current_time))
            sys.stdout.flush()
            if self.time_left.total_seconds() <= 0:
                # Play a sound file here.
                print "\nDone!"
            time.sleep(1)

    def pomodoro(self):
        self.run_duration(number_of_minutes=self.POMODORO_LENGTH)

    def long_break(self):
        self.run_duration(number_of_minutes=self.LONG_BREAK)

    def short_break(self):
        self.run_duration(number_of_minutes=self.SHORT_BREAK)

    def get_times(self):
        return {
            'current_time':  self.current_time,
            'end_time':      self.end_time,
            'time_left':     self.time_left
        }

    def update_times(self, end_time=None):
        self.current_time = datetime.datetime.now()
        if self.end_time:
            self.calculate_time_left()
        elif end_time:
            self.time_left = end_time - current_time_left
        else:
            raise PomodoroException("end_time was not specified.")


pomodoro = Pomodoro()
pomodoro.long_break()

print pomodoro.get_times()
