import sys
from tools.kterm import KTerm, TColor


"""
App's are instantiated at the beginning of the program. There should only be one instance of each app

Lifecycle: 
    * QUERY for information
    * INIT when app is selected, return True if everything worked, otherwise return error message
    * RUN called immediately after INIT if successful. This blocks and has its own GUI / input loop
    * DESTRUCT calls cleanup code and releases resources if necessary
"""

DEFAULT_FOREGROUND = TColor.White
DEFAULT_BACKGROUND = TColor.Black
DEFAULT_PROMPT = "Enter Input: "

class AppBase:
    def __init__(self, name, version, key, description, term: KTerm):
        self.term = term
        self.info = {
            "name": name,
            "version": version,
            "key": key,
            "description": description
        }

        # Used for terminal colors
        self.foreground = DEFAULT_FOREGROUND
        self.background = DEFAULT_BACKGROUND

        # Only true when app is running and showing on terminal
        self.active = False

    # --- PUBLIC ---
    def query_information(self):
        return self.info

    def initialize(self):
        return "App under construction"

    def run(self):
        self.term.initialize(self.foreground, self.background)
        self.term.clear_screen()

        char = 0
        while True:
            force_exit = self.update(char)
            if force_exit: return

            self.term.receive_input(char)
            self.term.render()

            self.prompt()

            # print(char)

            char = ord(sys.stdin.read(1))
            if char == 3:
                return

    def destruct(self):
        raise NotImplementedError

    # --- PRIVATE ---
    def update(self, input):
        raise NotImplementedError

    def prompt(self):
        self.term.print_line('')
        self.term.print_line('')

        self.term.print(DEFAULT_PROMPT)