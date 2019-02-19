from . import TColor
from .term_control import Control

"""
kwargs can include:
    * uppercase=False, lowercase=False,
    * [key/value]_foreground=White/Cyan, [key/value]_background=Black,
    * end_newline=True, [key/value]bold=False
    * symbol=": "
"""


class Textvalue(Control):
    def __init__(self, row, column, key, value, **kwargs):
        super().__init__(row, column)

        self.key = str(key)
        self.value = str(value)

        self.key_foreground = kwargs['key_foreground'] if 'key_foreground' in kwargs else TColor.White
        self.key_background = kwargs['key_background'] if 'key_background' in kwargs else TColor.Black
        self.value_foreground = kwargs['value_foreground'] if 'value_foreground' in kwargs else TColor.Cyan
        self.value_background = kwargs['value_background'] if 'value_background' in kwargs else TColor.Black

        if 'uppercase' in kwargs and kwargs['uppercase']:
            self.text = self.text.upper()

        if 'lowercase' in kwargs and kwargs['lowercase']:
            self.text = self.text.upper()

        self.has_newline = kwargs['end_newline'] if 'end_newline' in kwargs else True

        self.key_bold = kwargs['key_bold'] if 'key_bold' in kwargs else False
        self.value_bold = kwargs['value_bold'] if 'value_bold' in kwargs else True

        self.symbol = kwargs['symbol'] if 'symbol' in kwargs else ": "

    def get_size(self):
        width = len(self.key) + len(self.symbol) + len(self.value)
        return width % self.host.width, width // self.host.width + 1

    def render(self):
        self.host.set_color(self.key_foreground, self.key_background, self.key_bold)

        self.host.print(self.key)
        self.host.print(self.symbol)

        self.host.set_color(self.value_foreground, self.value_background, self.value_bold)
        if self.has_newline:
            self.host.print_line(self.value)
        else:
            self.host.print(self.value)








