from . import TColor
from .term_control import Control


class Header(Control):
    def __init__(self, row, column, text, **kwargs):
        super().__init__(row, column)

        self.text = text

    def get_size(self):
        return 12 + len(self.text), 1

    def render(self):
        self.host.set_color(TColor.White, TColor.Black, True)

        self.host.print(''.join(['-'] * 5))

        self.host.set_color(foreground=TColor.Cyan, bold=True)
        self.host.print(' %s ' % self.text)

        self.host.set_color(TColor.White, TColor.Black, True)
        self.host.print_line(''.join(['-'] * 5))







