from sqlite3 import OperationalError

from nose.tools import raises
from app.import_file.import_ofx import ImportOfx
from app.db import TestDb
from app.db.accounts import Accounts


class TestAccountTable:

    test_db = None
    ofx_data = None

    @classmethod
    def setup_class(cls):
        importer = ImportOfx('sample.ofx')
        cls.ofx_data = importer.import_ofx()


    def setup(self):
        self.test_db = TestDb.get_connection()

    def teardown(self):
        TestDb.close_connection()
        TestDb.destroy()

    def test_db_exists(self):
        assert self.test_db is not None

    @raises(OperationalError)
    def test_accounts_table_empty(self):
        cursor = self.test_db.cursor()
        cursor.execute('''SELECT * from accounts''')

    def test_accounts_create(self):
        accounts = Accounts(TestDb)
        accounts.create_table()
        count = accounts.count()
        assert count == 0

    def test_account_insert(self):
        accounts = Accounts(TestDb)
        accounts.create_table()
        pre_count = accounts.count()
        new_account = accounts.insert(self.ofx_data.bank_info)
        post_count = accounts.count()
        assert post_count == pre_count + 1
        print(new_account)
        assert new_account.id is not None
