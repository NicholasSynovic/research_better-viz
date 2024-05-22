import sqlite3

import pandas as pd

# Path to your modified SQL file
sql_file_path = "../Example-Data.db"

# Connect to (or create) the SQLite database
conn = sqlite3.Connection(database=sql_file_path)
df = pd.read_sql_query("SELECT * FROM cloc", con=conn)
conn.close()

print(df)
