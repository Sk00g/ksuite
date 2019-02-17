from . import TColor
from .term_control import Control

"""
kwargs can be any of:
    * symbol=*, prespace='  ', tab_matched=True

point_list: {
    "key": 'name',
    "value": 'Scott'
}
"""

class BulletList(Control):
    def __init__(self, row, column, point_list, **kwargs):
        super().__init__(row, column)

        self.point_list = point_list

        self.symbol = kwargs['symbol'] if 'symbol' in kwargs else '*'
        self.prespace = kwargs['prespace'] if 'prespace' in kwargs else '  '
        self.tab_matched = kwargs['tab_matched'] if 'tab_matched' in kwargs else True

    def render(self):
        # Find the farthest matching tab stop
        longest_key = 0
        for point in self.point_list:
            if 'key' in point and len(point['key']) > longest_key:
                longest_key = len(point['key'])

        for point in self.point_list:
            key = point['key'] if 'key' in point else None
            self.host.reset_color()

            if self.prespace:
                self.host.print(self.prespace)

            if key:
                self.host.print("%s %s: " % (self.symbol, key))

            if self.tab_matched and key:
                self.host.print(''.join([' '] * (longest_key - len(key) + 1)))

            if 'bold' in point and point['bold']:
                self.host.set_color(bold=True)

            self.host.print_line(str(point['value']))
