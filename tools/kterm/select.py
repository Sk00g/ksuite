from . import TColor, ARROWS
from .term_control import Control

"""
kwargs can be any of:
    * symbol=#(*,-,+,$,@), prespace='  '

symbol=# Will display 1. / 2. etc.

option_list: {
    "text": 'name',
    "action": func,
    "hotkey": '[^!]1'
}
"""

SYMBOLS = ['*', '-', '+', '$', '#', '@']

class Select(Control):
    def __init__(self, row, column, option_list, **kwargs):
        super().__init__(row, column)

        self.option_list = option_list

        self.symbol = kwargs['symbol'] if 'symbol' in kwargs else '#'
        self.prespace = kwargs['prespace'] if 'prespace' in kwargs else '  '

        self.focused_index = -1

    def receive_input(self, char):
        if char in ARROWS['down']:
            self.focused_index += 1
            if self.focused_index >= len(self.option_list):
                self.focused_index = 0
        elif char in ARROWS['up']:
            self.focused_index -= 1
            if self.focused_index < 0:
                self.focused_index = len(self.option_list) - 1
        elif char == 13:
            if self.focused_index in range(len(self.option_list)):
                self.option_list[self.focused_index]['action']()

    def get_size(self):

        longest_line = 0
        for option in self.option_list:
            symbol_width = 1
            length = len(self.prespace) + symbol_width + 1 + len(option['value'])
            if length > longest_line:
                longest_line = length

        return longest_line, len(self.option_list)

    def render(self):
        for ind in range(len(self.option_list)):
            option = self.option_list[ind]
            self.host.reset_color()

            bg = TColor.Cyan if ind == self.focused_index else TColor.Black
            self.host.set_color(background=bg)

            if self.prespace:
                self.host.print(self.prespace)

            if self.symbol in SYMBOLS:
                self.host.set_color(TColor.HackerGreen, bg, True)
                if self.symbol == '#':
                    self.host.print("(%d) " % (ind + 1))
                else:
                    self.host.print("(%s) " % self.symbol)

            self.host.set_color(TColor.White, bg, False)
            self.host.print_line(str(option['text']))