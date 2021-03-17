from tt.responses.response import ResponseSuccess


def test_response__is_true__when_response_is_successful():
    assert bool(ResponseSuccess()) is True