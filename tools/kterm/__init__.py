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

ARROWS = {
    'right': [67, 54, 100],
    'left': [68, 52, 97],
    'down': [66, 53 , 115],
    'up': [65, 56, 119]
}

from .kterm import KTerm
from .term_control import Control
from .textblock import Textblock
from .header import Header
from .title import Title
from .bullet_list import BulletList
from .select import Select