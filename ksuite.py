import tools.kterm as kterm
import sys
from tools.kterm import KTerm, TColor
from apps import *
import colorama

# Ensure color and cursor commands also work on Windows
colorama.init()

# Prepare terminal
term = KTerm()
options = None

apps = [
    DailyK(term), JView(term)
]

def run_app():
    active_app = apps[options.focused_index]
    active_app.initialize()
    active_app.run()
    active_app.destruct()

    run_app_selector()

def clean_exit():
    term.destruct()
    sys.exit(0)

def run_app_selector():
    global options

    term.initialize(TColor.White, TColor.Black)
    term.clear_screen()
    term.show_cursor(False)

    kterm.Title(0, 0, "K-SUITE V1.01")

    # Mutable 'selection' section
    app_info = {
        "title": kterm.Textblock(4, 5, "APP NAME: -"),
        "version": kterm.Textblock(4, 6, "APP VERSION: -"),
        "key": kterm.Textblock(4, 7, "APP KEY: -"),
        "description": kterm.Textblock(4, 8, "- "),
    }
    for ctrl in app_info.values():
        ctrl.visible = False

    kterm.Header(0, 10, "Available Apps")

    app_options = []
    for apption in apps:
        app_options.append({
            "text": apption.query_information()["name"],
            "action": lambda: run_app()
        })
    app_options.append({"text": "Exit", "action": lambda: clean_exit()})

    options = kterm.Select(0, 11, app_options)
    options.focused_index = 0

    kterm.Textblock(0, 15 + len(app_options), "Select an app to run or exit...")

    char = 0
    while True:
        term.receive_input(char)
        options.receive_input(char)

        if options.focused_index != len(options.option_list) - 1:
            info = apps[options.focused_index].query_information()
            app_info["title"].text = "APP NAME: %s" % info["name"]
            app_info["version"].text = "APP VERSION: %s" % info["version"]
            app_info["key"].text = "APP KEY: %s" % info["key"]
            app_info["description"].text = "- %s" % info["description"]

        for ctrl in app_info.values():
            ctrl.visible = options.focused_index != len(options.option_list) - 1

        term.render()

        char = ord(sys.stdin.read(1))
        if char == 3:
            clean_exit()

try:
    run_app_selector()

except Exception as err:
    term.destruct()
    print('finished with exception: %s' % (str(err)))
