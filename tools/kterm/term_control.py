
class Control:
    # --- KTerminal Singleton ---
    Host = None

    def __init__(self, row, column):
        self.start = row, column

        self.visible = True

        self.host = Control.Host
        self.host.control_list.append(self)
        self.section = None

    def enter_section(self, section):
        self.section = section
        self.host.control_list.remove(self)

    def leave_section(self):
        self.section = None
        self.host.control_list.append(self)

    def get_size(self):
        raise NotImplementedError


    @staticmethod
    def set_host(host_terminal):
        Control.Host = host_terminal
