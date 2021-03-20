from tt.repository.memrepo import MemRepo
from tt.responses.response import (ResponseFailure, ResponseSuccess,
                                   ResponseTypes,
                                   build_response_from_invalid_request)


def time_entry_list_use_case(repo: MemRepo, request):
    if not request:
        return build_response_from_invalid_request(request)
    try:
        time_entries = repo.list(filters=request.filters)
        return ResponseSuccess(time_entries)
    except Exception as e:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, e)
