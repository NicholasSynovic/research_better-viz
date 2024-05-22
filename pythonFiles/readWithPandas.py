# importing stuff
import sqlite3

import pandas as pd

# Path to .db file
sql_file_path = "../Example-Data.db"

# Connect to the SQLite database
conn = sqlite3.Connection(database=sql_file_path)
df = pd.read_sql_query("SELECT * FROM cloc LIMIT 10", con=conn)
conn.close()

print(df)
