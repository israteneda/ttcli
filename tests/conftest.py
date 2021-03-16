import pytest

from application.rest.app import create_app


@pytest.fixture
def app():
    app = create_app("testing")

    return app
