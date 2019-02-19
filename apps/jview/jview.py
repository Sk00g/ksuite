import os
import sys
import tools.kterm as term
from apps.app_base import AppBase
from .enums import *


APP_NAME = "J Viewer"
APP_VERSION = "V1.01.190218"
APP_KEY = "jview"
APP_DESCRIPTION = "JSON viewing application to view and edit JSON file data."

class ModeState:
    def __init__(self, host_app):
        self.host = host_app
        self.term = self.host.term

class EditState(ModeState):
    def update(self, input):
        pass

class SearchState(ModeState):
    def update(self, input):
        pass

class NavigateState(ModeState):
    def update(self, input):
        pass

class FileViewerState(ModeState):
    def __init__(self, host_app):
        super().__init__(host_app)

        self.cur_dir = os.path.join(os.getcwd(), "pdata", "store")
        self.file_list = [file for file in os.listdir(self.cur_dir) if file.endswith(".json")]
        self.dir_list = [dir for dir in os.listdir(self.cur_dir) if dir.find('.') == -1]

        height = 4
        self.location_text = term.Textvalue(0, height, "LOC",
            (self.cur_dir if len(self.cur_dir) < 30 else ("(...)" + self.cur_dir[-35:])))
        self.file_text = term.Textvalue(self.term.width - 18, height, "FILES", len(self.file_list))
        self.dir_text = term.Textvalue(self.term.width - 8, height, "DIRS", len(self.dir_list))

        

    def update(self, input):
        pass

class JView(AppBase):
    def __init__(self, terminal):
        super().__init__(APP_NAME, APP_VERSION, APP_KEY, APP_DESCRIPTION, terminal)

        self.state_list = {}

        self.active_state = None
        self.state_text = None

    def swap_state(self, new_state):
        pass

    def initialize(self):
        super().initialize()

        self.state_list = {
            Mode.FILE_VIEWER: FileViewerState(self),
            Mode.NAVIGATE: NavigateState(self),
            Mode.SEARCH: SearchState(self),
            Mode.EDIT: EditState(self)
        }

        term.Title(0, 0, "JSON Viewer")

        # Begin in Mode.FILE_VIEWER state
        self.active_state = self.state_list[Mode.FILE_VIEWER]

        state_text = [key for key in self.state_list if self.state_list[key] == self.active_state][0]
        self.state_text = term.Textblock(self.term.width - len(state_text), self.term.height, state_text)

        return True

    def destruct(self):
        pass

    def update(self, input):
        self.active_state.update(input)

        return False

    def prompt(self):
        pass

