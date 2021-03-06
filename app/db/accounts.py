from app.ofx.ofx_bank import OfxBank


class Accounts:

    connection = None

    def __init__(self, manager):
        self.connection = manager.get_connection()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute((
            'CREATE TABLE accounts('
            ' id INTEGER PRIMARY KEY ,'
            ' alias TEXT,'
            ' routing_number INTEGER,'
            ' account_number INTEGER,'
            ' account_type TEXT',
            ' balance REAL,'
            ' available_balance REAL)'
        ))
        self.connection.commit()

    def count(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT count(*) FROM accounts')
        row = cursor.fetchone()
        return row[0]

    def insert(self, account_obj: OfxBank):
        cursor = self.connection.cursor()
        sql = (
            'INSERT INTO accounts'
            ' ( routing_number, account_number, account_type, balance, available_balance ) '
            ' VALUES '
            ' ( ?, ?, ?, ? )'
        )
        data = (
            account_obj.routing_number,
            account_obj.account_number,
            account_obj.account_type,
            account_obj.balance,
            account_obj.available_balance
        )
        cursor.execute(sql, data)
        cursor.execute("SELECT last_insert_rowid()")
        rowid = cursor.fetchone()
        self.connection.commit()
        account_obj.id = rowid[0]

        return account_obj
