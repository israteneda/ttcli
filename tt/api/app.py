from datetime import datetime

from flask import Flask

from tt.domain.time_entry import TimeEntry

app = Flask(__name__)


@app.route('/clock-in')
def clock_in():
    time_entry: TimeEntry = TimeEntry()
    time_entry.start = datetime.now()
    return f"You start a time entry at {time_entry.start}"
