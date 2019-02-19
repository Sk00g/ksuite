from . import TColor
from .term_control import Control

"""
kwargs can include:
    * uppercase=False, lowercase=False,
    * foreground=TColor.White, background=TColor.Black,
    * end_newline=True, bold=False
"""


class Textblock(Control):
    def __init__(self, row, column, text, **kwargs):
        super().__init__(row, column)

        self.text = str(text)
        self.foreground = kwargs['foreground'] if 'foreground' in kwargs else TColor.White
        self.background = kwargs['background'] if 'background' in kwargs else TColor.Black

        if 'uppercase' in kwargs and kwargs['uppercase']:
            self.text = self.text.upper()

        if 'lowercase' in kwargs and kwargs['lowercase']:
            self.text = self.text.upper()

        self.has_newline = kwargs['end_newline'] if 'end_newline' in kwargs else True

        self.bold = kwargs['bold'] if 'bold' in kwargs else False

    def get_size(self):
        return len(self.text) % self.host.width, len(self.text) // self.host.width + 1

    def render(self):
        self.host.set_color(self.foreground, self.background, self.bold)

        if self.has_newline:
            self.host.print_line(self.text)
        else:
            self.host.print(self.text)







