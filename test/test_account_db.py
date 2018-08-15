from app.db import TestDb


test_db = None


def setup():
    global test_db
    test_db = TestDb.get_connection()
    print(test_db)


def teardown():
    TestDb.close_connection()
    pass


def test_db_exists():
    assert test_db is not None
