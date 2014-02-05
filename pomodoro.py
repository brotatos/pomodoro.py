#!/usr/bin/env python2
import time
from datetime import datetime, timedelta
import sys


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

    def calculate_time_left(self):
        self.time_left = self.end_time - self.current_time

    def run_duration(self, number_of_minutes):
        time_duration = timedelta(minutes=number_of_minutes)
        self.end_time = self.current_time + time_duration
        self.calculate_time_left()
        self.countdown()

    def countdown(self):
        while self.time_left.total_seconds() > 0:
            self.update_times()
            self.print_time_left()
            self.alert_end_of_period()

    def print_time_left(self):
        sys.stdout.write("\r" + str(self.end_time - self.current_time))
        sys.stdout.flush()

    def alert_end_of_period(self):
        if self.time_left.total_seconds() <= 0:
            # Play a sound file here.
            print "\n\aDone!"
        else:
            time.sleep(1)

    def do_pomodoro(self):
        self.run_duration(number_of_minutes=self.POMODORO_LENGTH)

    def take_long_break(self):
        self.run_duration(number_of_minutes=self.LONG_BREAK)

    def take_short_break(self):
        self.run_duration(number_of_minutes=self.SHORT_BREAK)

    def get_times(self):
        return {
            'current_time':  self.current_time,
            'end_time':      self.end_time,
            'time_left':     self.time_left
        }

    def update_times(self, end_time=None):
        self.current_time = datetime.now()
        if self.end_time:
            self.calculate_time_left()
        elif end_time:
            self.time_left = end_time - self.current_time
        else:
            raise PomodoroException("end_time was not specified.")


pomodoro = Pomodoro()
pomodoro.take_short_break()

print pomodoro.get_times()
