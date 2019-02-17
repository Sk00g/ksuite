from tools.kterm import KTerm
from apps.dailyK import DailyK





# Prepare terminal
term = KTerm()


app = DailyK(term)
try:
    app.initialize()
    app.run()
    app.destruct()

    # finish cleanly
    term.destruct()
except Exception as err:
    term.destruct()
    print('finished with exception: %s' % (str(err)))
