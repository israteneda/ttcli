import pytest
import sqlalchemy
from tt.repository.postgres_objects import Base, TimeEntry


@pytest.fixture(scope="session")
def pg_session_empty(app_configuration):
    conn_str = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
        app_configuration["POSTGRES_USER"],
        app_configuration["POSTGRES_PASSWORD"],
        app_configuration["POSTGRES_HOSTNAME"],
        app_configuration["POSTGRES_PORT"],
        app_configuration["APPLICATION_DB"],
    )
    engine = sqlalchemy.create_engine(conn_str)
    connection = engine.connect()

    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    DBSession = sqlalchemy.orm.sessionmaker(bind=engine)
    session = DBSession()

    yield session

    session.close()
    connection.close()


@pytest.fixture(scope="session")
def pg_test_data():
    return [
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


@pytest.fixture(scope="function")
def pg_session(pg_session_empty, pg_test_data):
    for time_entry in pg_test_data:
        new_time_entry = TimeEntry(
            code=time_entry["code"],
            project=time_entry["project"],
            start_date=time_entry["start_date"],
            end_date=time_entry["end_date"],
            description=time_entry["description"],
        )

    yield pg_session_empty

    pg_session_empty.query(TimeEntry).delete()