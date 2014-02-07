#!/usr/bin/env python
import sys
from pomodoro import Pomodoro


class Console(object):

    def __init__(self):
        self.pomodoro = Pomodoro()

    def ask_question(self):
        while True:
            print("(p)omodoro, (l)ong break, (s)hort break, (q)uit")
            response = input("> ")
            self.do_pomodoro_action(response)

    def do_pomodoro_action(self, letter):
        if letter == 'p':
            self.pomodoro.do_pomodoro()
        elif letter == 'l':
            self.pomodoro.take_long_break()
        elif letter == 's':
            self.pomodoro.take_short_break()
        elif letter == 'q':
            sys.exit(0)
        else:
            print("Type p, l, or s to select our choice.")
            self.ask_question()


console = Console()
console.ask_question()
