from tt.responses.response import ResponseTypes

STATUS_CODE = {
    ResponseTypes.SUCCESS: 200,
    ResponseTypes.RESOURCE_ERROR: 404,
    ResponseTypes.PARAMETERS_ERROR: 400,
    ResponseTypes.SYSTEM_ERROR: 500,
}

TIME_ENTRIES = [
    {
        "code": "0d3cf93b-c443-4949-adf8-06828a92f404",
        "project": "ioet Inc. - ioet-internal",
        "start_date": "09:00:00",
        "end_date": "10:00:00",
        "description": "Time Tracker CLI developments",
    },
    {
        "code": "ab7a8a9a-6c0e-4a86-935b-9f3e377471cd",
        "project": "ioet Inc. - ioet-internal",
        "start_date": "10:00:00",
        "end_date": "11:00:00",
        "description": "Time Tracker CLI developments",
    },
    {
        "code": "acf285db-e378-43a7-8ddd-c18c4fe1d693",
        "project": "ioet Inc. - ioet-internal",
        "start_date": "11:00:00",
        "end_date": "12:00:00",
        "description": "Time Tracker CLI developments",
    },
    {
        "code": "e025b74f-ae25-45a0-b082-0fde2cb56fc6",
        "project": "ioet Inc. - ioet-internal",
        "start_date": "12:00:00",
        "end_date": "13:00:00",
        "description": "Time Tracker CLI developments",
    },
]
