from tt.request.time_entry_list_request import TimeEntryListInvalidRequest
from tt.responses.response import (ResponseFailure, ResponseSuccess,
                                   ResponseTypes,
                                   build_response_from_invalid_request)

SUCCESS_VALUE = {"key": ["value1", "value2"]}
GENERIC_RESPONSE_TYPE = "Response"
GENERIC_RESPONSE_MESSAGE = "This is a response"


def test_response__it_is_true__when_response_is_successful():
    response = ResponseSuccess(SUCCESS_VALUE)

    assert bool(response) is True


def test_response__it_is_false__when_response_failure():
    response = ResponseFailure(GENERIC_RESPONSE_TYPE, GENERIC_RESPONSE_MESSAGE)

    assert bool(response) is False


def test_response__there_is_type_and_value__when_response_is_successful():
    response = ResponseSuccess(SUCCESS_VALUE)

    assert response.type == ResponseTypes.SUCCESS
    assert response.value == SUCCESS_VALUE


def test_response__there_is_type_and_message__when_response_failure():
    response = ResponseFailure(GENERIC_RESPONSE_TYPE, GENERIC_RESPONSE_MESSAGE)

    assert response.type == GENERIC_RESPONSE_TYPE
    assert response.message == GENERIC_RESPONSE_MESSAGE
    assert response.value == {
        "type": GENERIC_RESPONSE_TYPE,
        "message": GENERIC_RESPONSE_MESSAGE,
    }


def test_response__return_exception_message__when_the_response_fails():
    response = ResponseFailure(
        GENERIC_RESPONSE_TYPE, Exception("Just an error message")
    )

    assert bool(response) is False
    assert response.type == GENERIC_RESPONSE_TYPE
    assert response.message == "Exception: Just an error message"


def test_response__it_is_false__when_invalid_request_is_empty():
    response = build_response_from_invalid_request(TimeEntryListInvalidRequest())

    assert bool(response) is False
    assert response.type == ResponseTypes.PARAMETERS_ERROR


def test_response__it_is_false__when_invalid_request_has_errors():
    request = TimeEntryListInvalidRequest()
    request.add_error("path", "Is mandatory")
    request.add_error("path", "can't be blank")

    response = build_response_from_invalid_request(request)

    assert bool(response) is False
    assert response.type == ResponseTypes.PARAMETERS_ERROR
    assert response.message == "path: Is mandatory\npath: can't be blank"
