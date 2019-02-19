from . import Direction
from .term_control import Control

"""
kwargs can include:
    * margin=2
    * columns=1, column_margin=4 (only apply if direction=vertical)
    * rows=1, row_margin=4 (only apply if direction=horizontal)
    * direction=down[right/left/up]
"""


class Section(Control):
    def __init__(self, row, column, **kwargs):
        super().__init__(row, column)

        self.margin = kwargs['margin'] if 'margin' in kwargs else 2
        self.columns = kwargs['columns'] if 'columns' in kwargs else 1
        self.column_margin = kwargs['column_margin'] if 'column_margin' in kwargs else 4
        self.rows = kwargs['rows'] if 'rows' in kwargs else 1
        self.row_margin = kwargs['row_margin'] if 'row_margin' in kwargs else 4
        self.direction = kwargs['direction'] if 'direction' in kwargs else Direction.DOWN

        self.control_list = []

        self.last_placement = -1, -1

    # auto_place=True generates the 'start' property of the control based on section settings
    def add_control(self, ctrl: Control, auto_place=True):
        self.control_list.append(ctrl)
        ctrl.enter_section(self)

        # Handle auto-arrangement
        if auto_place:
            if self.direction == Direction.DOWN:
                newy = self.last_placement[0]
                newx = 0
                self.last_placement

    def remove_control(self, ctrl):
        if ctrl in self.control_list:
            self.control_list.remove(ctrl)
            ctrl.leave_section(self)

    def render(self):
        for ctrl in [c for c in self.control_list if c.visible]:
            self.host.set_cursor(self.start[0] + ctrl.start[0], self.start[1] + ctrl.start[1])
            ctrl.render()








