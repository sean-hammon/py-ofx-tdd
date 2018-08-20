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
        sql = f"INSERT INTO migrations (filename, executed_at) VALUES ('{migration}', date('now'))"
        cursor.execute(sql)
        with open(f'./sqlite/migrations/{migration}') as file:
            sql = file.read()
            cursor.execute(sql)
        connection.commit()

print(migration_files)
