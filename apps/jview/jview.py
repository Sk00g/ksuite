import os
import sys
import tools.kterm as term
from apps.app_base import AppBase
from .enums import *


APP_NAME = "J Viewer"
APP_VERSION = "V1.01.190218"
APP_KEY = "jview"
APP_DESCRIPTION = "JSON viewing application to view and edit JSON file data."


class EditState:
    def update(self, input):
        pass

class SearchState:
    def update(self, input):
        pass

class NavigateState:
    def update(self, input):
        pass

class FileViewerState:
    def __init__(self):
        self.cur_dir = os.path.join(os.getcwd(), "pdata", "store")
        self.file_list = [file for file in os.listdir(self.cur_dir) if file.endswith(".json")]
        self.dir_list = [dir for dir in os.listdir(self.cur_dir) if dir.find('.') == -1]

        self.location_text = term.Textblock(0, 4, "LOC: %s" % self.cur_dir[-10:])
        self.file_text = term.Textblock(18, 4, "FILES: %d" % len(self.file_list))
        self.dir_text = term.Textblock(28, 4, "DIRS: %d" % len(self.dir_list))

    def update(self, input):
        pass

class JView(AppBase):
    def __init__(self, terminal):
        super().__init__(APP_NAME, APP_VERSION, APP_KEY, APP_DESCRIPTION, terminal)

        self.state_list = {
            Mode.FILE_VIEWER: FileViewerState(),
            Mode.NAVIGATE: NavigateState(),
            Mode.SEARCH: SearchState(),
            Mode.EDIT: EditState(),
        }

        # Begin in Mode.FILE_VIEWER state
        self.active_state = self.state_list[Mode.FILE_VIEWER]

    def swap_state(self, new_state):
        pass

    def initialize(self):
        super().initialize()
        self.term.show_cursor(True)

        term.Title(0, 0, "JSON Viewer")

        return True

    def destruct(self):
        pass

    def update(self, input):
        self.active_state.update(input)

        return False

    def prompt(self):
        super().prompt()

