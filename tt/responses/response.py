class ResponseTypes:
    PARAMETERS_ERROR = "ParametersError"
    RESOURCE_ERROR = "ResourcesError"
    SYSTEM_ERROR = "SystemError"
    SUCCESS = "Success"


def _format_message(msg):
    if isinstance(msg, Exception):
        return f"{msg.__class__.__name__}: {msg}"
    return msg


class ResponseFailure:
    def __init__(self, type_, message):
        self.type = type_
        self.message = _format_message(message)

    @property
    def value(self):
        return {"type": self.type, "message": self.message}

    def __bool__(self):
        return False


class ResponseSuccess:
    def __init__(self, value=None):
        self.type = ResponseTypes.SUCCESS
        self.value = value

    def __bool__(self):
        return True


def build_response_from_invalid_request(invalid_request):
    message = "\n".join(
        [f"{err['parameter']}: {err['message']}" for err in invalid_request.errors]
    )
    return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, message)
