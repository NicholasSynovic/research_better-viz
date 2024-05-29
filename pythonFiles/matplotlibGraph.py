# importing stuff
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd

# Path to .db file
sql_file_path = "../Example-Data.db"

# Connect to the SQLite database
conn = sqlite3.Connection(database=sql_file_path)
df = pd.read_sql_query("SELECT * FROM cloc LIMIT 10", con=conn)
conn.close()

print(df)

# plot stats

df.plot.line(x="index", y="file_count")
plt.ylabel("file_count")
plt.title("index and file count")
plt.tight_layout()
plt.savefig("test.png")
