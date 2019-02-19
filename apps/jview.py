import tools.kterm as term
from apps.app_base import AppBase


APP_NAME = "J Viewer"
APP_VERSION = "V1.01.190218"
APP_KEY = "jview"
APP_DESCRIPTION = "JSON viewing application to view and edit JSON file data."


class JView(AppBase):
    def __init__(self, terminal):
        super().__init__(APP_NAME, APP_VERSION, APP_KEY, APP_DESCRIPTION, terminal)

    def initialize(self):
        term.Title(0, 0, "JSON Viewier")

        term.Textblock(0, 2, "Hello my name is reginald and I like cake")

        return True

    def destruct(self):
        pass

    def update(self, input):
        return False

    def prompt(self):
        super().prompt()

