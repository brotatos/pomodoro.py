from sys import exit
from pomodoro import Pomodoro


class Console(object):

    def __init__(self):
        self.pomodoro = Pomodoro()
        self.commands = {
            'p': self.pomodoro.do_pomodoro,
            'l': self.pomodoro.take_long_break,
            's': self.pomodoro.take_short_break,
            'q': exit
        }
        self.question = "(p)omodoro, (l)ong break, (s)hort break, (q)uit"
        self.correction = "Type p, l, or s to select our choice."

    def ask_question(self):
        while True:
            print(self.question)
            response = raw_input("> ")
            self.do_pomodoro_action(response)

    def do_pomodoro_action(self, letter):
        if letter in self.commands.keys():
            self.commands[letter]()
        else:
            print(self.correction)
            self.ask_question()
