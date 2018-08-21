from sqlite3 import OperationalError
import os

from app.db import LiveDb

connection = LiveDb.get_connection()
cursor = connection.cursor()
try:
    result = cursor.execute("SELECT * FROM migrations WHERE executed_at IS NULL")
    rows = result.fetchall()
    completed = [r.filename for r in rows]
    print(completed)
except OperationalError:
    cursor.execute(
        'CREATE TABLE migrations ('
        ' filename TEXT,'
        ' executed_at TEXT'
        ')'
    )
    completed = []

migration_files = os.listdir('./sqlite/migrations')
for migration in migration_files:
    if migration not in completed:
        sql = "INSERT INTO migrations (filename, executed_at) VALUES ('{}', date('now'))".format(migration)
        cursor.execute(sql)
        with open('./sqlite/migrations/{}'.format(migration)) as file:
            sql = file.read()
            cursor.execute(sql)
        connection.commit()

print(migration_files)
