from tt.responses.response import ResponseSuccess


def time_entry_list_use_case(repo, request):
    time_entries = repo.list()
    return ResponseSuccess(time_entries)