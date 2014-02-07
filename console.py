#!/usr/bin/env python
from pomodoro import Pomodoro


class Console(object):

    def __init__(self):
        self.pomodoro = Pomodoro()

    def ask_question(self):
        print("(p)omodoro, (l)ong break, (s)hort break")


console = Console()
console.ask_question()
