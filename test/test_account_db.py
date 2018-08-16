from sqlite3 import OperationalError

from nose.tools import raises
from app.import_file.import_ofx import ImportOfx
from app.db import TestDb


class TestAccountTable:

    test_db = None
    ofx_data = None

    def setup(self):
        importer = ImportOfx('sample.ofx')
        self.ofx_data = importer.import_ofx()
        self.test_db = TestDb.get_connection()

    def teardown(self):
        TestDb.close_connection()

    def test_db_exists(self):
        assert self.test_db is not None

    @raises(OperationalError)
    def test_accounts_table_empty(self):
        cursor = self.test_db.cursor()
        cursor.execute('''SELECT * from accounts''')
