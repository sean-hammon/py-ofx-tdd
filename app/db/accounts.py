class Accounts:

    connection = None

    def __init__(self, manager):
        self.connection = manager.get_connection()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute((
            'CREATE TABLE accounts('
            ' id INTEGER PRIMARY KEY,'
            ' alias TEXT,'
            ' routing_number INTEGER,'
            ' account_number INTEGER,'
            ' balance REAL,'
            ' available_balance REAL)'
        ))
        self.connection.commit()

    def count(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT count(*) FROM accounts')
        row = cursor.fetchone()
        return row[0]

