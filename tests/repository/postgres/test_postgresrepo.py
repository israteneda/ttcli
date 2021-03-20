import pytest

from tt.repository.postgres_objects import TimeEntry

pytestmark = pytest.mark.integration


def test_repository_postgresrepo_dummy_test(pg_session):
    assert len(pg_session.query(TimeEntry).all()) == 0
