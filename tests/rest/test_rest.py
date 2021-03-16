def test_rest__set_time_tracker_start__when_calling_clock_in_function(client):
    http_response = client.get('/clock-in')

    assert "You start a time entry at" in http_response.data.decode("UTF-8")
