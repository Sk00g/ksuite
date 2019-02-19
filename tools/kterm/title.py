from . import TColor
from .term_control import Control


class Title(Control):
    def __init__(self, row, column, text, **kwargs):
        super().__init__(row, column)

        self.text = text

    def get_size(self):
        return self.host.width, 3

    def render(self):
        star_line = ['*'] * self.host.width
        title_start = self.host.width // 2 - len(self.text) // 2

        self.host.set_color(TColor.Cyan, TColor.Black, True)
        self.host.print_line(''.join(star_line))
        self.host.set_color(foreground=TColor.HackerGreen, bold=True)
        self.host.print(''.join(['*'] * (title_start - 1)))
        self.host.print(' ' + self.text + ' ')
        self.host.print_line(''.join(['*'] * (title_start - 1)))
        self.host.set_color(foreground=TColor.Cyan, bold=True)
        self.host.print_line(''.join(star_line))
        self.host.reset_color()
        self.host.print('\n\n')






