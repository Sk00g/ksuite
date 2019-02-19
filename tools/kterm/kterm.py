import sys
import tty
import fcntl, termios, struct
from . import TColor
from .term_control import Control


CONTROL_MARGIN = 2

class KTerm:
    def __init__(self):
        term_info = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
        self.height, self.width, self.hp, self.wp = term_info

        self._original_settings = termios.tcgetattr(sys.stdin.fileno())
        self._default_foreground, self._default_background = TColor.White, TColor.Black

        self.control_list = []

        # Assume singleton, and set host for all future created controls
        Control.set_host(self)

    # --- PUBLIC ---
    def render(self):
        self.clear_screen()
        self.reset_color()

        for ctrl in [c for c in self.control_list if c.visible]:
            self.set_cursor(ctrl.start[0], ctrl.start[1])
            ctrl.render()

        self.reset_color()

    def receive_input(self, char):
        pass

    def initialize(self, default_foreground, default_background):
        self.control_list = []
        self._default_foreground = default_foreground
        self._default_background = default_background
        self.reset_color()
        tty.setraw(sys.stdin)

    def destruct(self):
        # tty.setcbreak(sys.stdin)
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, self._original_settings)
        self._send('39m')
        self._send('49m')
        self.show_cursor(True)
        self.clear_screen()

    def show_cursor(self, flag):
        if flag:
            self._send('?25h')
        else:
            self._send('?25l')

    # --- PRIVATE ---


    def _send(self, data):
        sys.stdout.write('\u001b[' + data)

    def print(self, text):
        lines = text.split('\n')

        for i in range(0, len(lines) - 1):
            sys.stdout.write(lines[i])
            self._send('1B')
            self._send('0G')

        sys.stdout.write(lines[-1])
        sys.stdout.flush()

    def print_line(self, text):
        sys.stdout.write(text)
        self._send('1E')
        sys.stdout.flush()

    def set_cursor(self, x, y=-1):
        if y == -1:
            self._send('%dG' % x)
        else:
            self._send('%d;%dH' % (y, x))
        sys.stdout.flush()

    def clear_screen(self):
        self._send('2J')
        self.set_cursor(0, 0)

    def set_color(self, foreground=-1, background=-1, bold=False):
        self._send('0m')

        fg = self._default_foreground if foreground == -1 else foreground
        bg = self._default_background if background == -1 else background

        if bold:
            self._send('1m')

        self._send('38;5;%dm' % fg)
        self._send('48;5;%dm' % bg)

    def reset_color(self):
        self._send('0m')
        self.set_color(self._default_foreground, self._default_background)