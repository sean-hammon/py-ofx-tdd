from app.db import TestDb


class TestAccountTable:

    test_db = None

    def setup(self):
        self.test_db = TestDb.get_connection()

    def teardown(self):
        self.test_db.close_connection()

    def test_db_exists(self):
        assert self.test_db is not None
