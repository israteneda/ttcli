from application.rest.app import app


def test_rest__set_time_tracker_start__when_calling_clock_in_function():
    with app.test_client() as client:
        rv = client.get('/clock-in')
    assert b'You start a time entry at ' in rv.data
