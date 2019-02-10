import sys
import tty
import fcntl, termios, struct


class TColor:
    Black = 232
    Red = 1
    Green = 2
    Yellow = 3
    Blue = 4
    Magenta = 5
    Cyan = 6
    White = 7
    HackerGreen = 40


class KTerm:
    def __init__(self):
        term_info = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
        self.height, self.width, self.hp, self.wp = term_info

        self._original_settings = termios.tcgetattr(sys.stdin.fileno())
        self._default_foreground, self._default_background = TColor.White, TColor.Black

    def initialize(self, default_foreground, default_background):
        self._default_foreground = default_foreground
        self._default_background = default_background
        self.reset_color()
        tty.setraw(sys.stdin)

    def destruct(self):
        # tty.setcbreak(sys.stdin)
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, self._original_settings)
        self._send('39m')
        self._send('49m')
        self.clear_screen()

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

    def print_bullets(self, point_list, symbol="*", prespace='  ', tab_matched=True):
        # Find the farthest matching tab stop
        longest_key = 0
        for point in point_list:
            if 'key' in point and len(point['key']) > longest_key:
                longest_key = len(point['key'])

        for point in point_list:
            key = point['key'] if 'key' in point else None
            self.reset_color()

            if prespace:
                self.print(prespace)

            if key:
                self.print("%s %s: " % (symbol, key))

            if tab_matched and key:
                self.print(''.join([' '] * (longest_key - len(key) + 1)))

            if 'bold' in point and point['bold']:
                self.set_color(bold=True)

            self.print_line(str(point['value']))

    def print_header(self, text):
        self.reset_color()
        self.print(''.join(['-'] * 5))

        self.set_color(foreground=TColor.Cyan, bold=True)
        self.print(' %s ' % text)

        self.reset_color()
        self.print_line(''.join(['-'] * 5))

    def print_title(self, title):
        star_line = ['*'] * self.width
        title_start = self.width // 2 - len(title) // 2

        self.set_color(foreground=TColor.Cyan, bold=True)
        self.print_line(''.join(star_line))

        self.set_color(foreground=TColor.HackerGreen, bold=True)

        self.print(''.join(['*'] * (title_start - 1)))
        self.print(' ' + title + ' ')
        self.print_line(''.join(['*'] * (title_start - 1)))

        self.set_color(foreground=TColor.Cyan, bold=True)
        self.print_line(''.join(star_line))

        self.reset_color()
        self.print('\n\n')
