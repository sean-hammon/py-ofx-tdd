CREATE TABLE ledger (
     id INTEGER PRIMARY KEY ,
     account_id INTEGER 
     name TEXT,
     alias TEXT,
     memo TEXT,
     type TEXT,
     date_posted TEXT,
     amount REAL,
     check_number INTEGER,
     fitid TEXT
);

CREATE INDEX IF NOT EXISTS transaction_account_idx ON ledger (account_id);