import pytest

from tt.request.time_entry_list_request import build_time_entry_list_request


def test_requests_time_entry_list__build_time_entry_list__when_a_request_is_made_without_parameters():
    request = build_time_entry_list_request()

    assert request.filters is None
    assert bool(request) is True


def test_requests_time_entry_list__build_time_entry_list__when_a_request_is_made_from_empty_dict():
    request = build_time_entry_list_request({})

    assert request.filters == {}
    assert bool(request) is True


def test_requests_time_entry_list__return_an_error_and_false_status_for_request__when_invalid_arguments_are_passed():
    request = build_time_entry_list_request(filters=5)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "filters"
    assert bool(request) is False


def test_requests_time_entry_list__return_an_error_and_false_status_for_request__when_incorrect_filter_keys():
    request = build_time_entry_list_request(filters={"a": 1})

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "filters"
    assert bool(request) is False


@pytest.mark.parametrize(
    "key",
    [
        "code__eq",
        "project__eq",
        "date_in__lt",
        "date_in__gt",
        "date_out__lt",
        "date_out__gt",
        ],
    )
def test_requests_time_entry_list__return_true__when_filters_are_accepted(key):
    filters = {key: 1}

    request = build_time_entry_list_request(filters=filters)

    assert request.filters == filters
    assert bool(request) is True


@pytest.mark.parametrize("key", ["code__lt", "code__gt"])
def test_requests_time_entry_list__return_false__when_filters_are_rejected(key):
    filters = {key: 1}

    request = build_time_entry_list_request(filters=filters)
    assert request.errors[0]["parameter"] == "filters"
    assert bool(request) is False