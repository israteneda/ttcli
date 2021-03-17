from tt.request.time_entry_list_request import TimeEntryListRequest


def test_time_entry_list__build_time_entry_list__when_a_request_is_made_without_parameters():
    request = TimeEntryListRequest()

    assert bool(request) is True

def test_time_entry_list__build_time_entry_list__when_a_request_is_made_from_empty_dict():
    request = TimeEntryListRequest.from_dict({})

    assert bool(request) is True
