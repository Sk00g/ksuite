from tools.kterm import KTerm, TColor
from apps.dailyK import DailyK


DEFAULT_FOREGROUND = TColor.White
DEFAULT_BACKGROUND = TColor.Black


# Prepare terminal
term = KTerm()
term.initialize(DEFAULT_FOREGROUND, DEFAULT_BACKGROUND)
term.clear_screen()


app = DailyK(term)
try:
    app.run()

    # finish cleanly
    term.destruct()
except Exception as err:
    term.destruct()
    print('finished with exception: %s' % (str(err)))

