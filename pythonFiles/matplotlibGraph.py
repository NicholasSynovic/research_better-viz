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

# print stats onto terminal
print(df["file_count"][0:10])

# plot stats
plt.locator_params(axis="x", integer=True)
df.plot.line(x="index", y="file_count", color="red")
plt.savefig("test.png")