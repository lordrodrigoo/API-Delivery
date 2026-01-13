#pylint: disable=redefined-outer-name
import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler

@pytest.fixture(scope="module")
def db_connection():
    handler = DBConnectionHandler()
    conn = handler.get_engine().connect()
    yield conn
    conn.close()


@pytest.fixture
def teardown(db_connection):
    def _teardown(query):
        db_connection.execute(text(query))
        db_connection.commit()
    return _teardown
