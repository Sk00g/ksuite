
class Control:
    # --- KTerminal Singleton ---
    Host = None

    def __init__(self, row, column):
        self.start = row, column

        self.width, self.height = 0, 0
        self.visible = True

        self.host = Control.Host
        self.host.control_list.append(self)

    @staticmethod
    def set_host(host_terminal):
        Control.Host = host_terminal
