# importing stuff
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Path to .db file
sql_file_path = "../Example-Data.db"

# Connect to the SQLite database
conn = sqlite3.Connection(database=sql_file_path)
df = pd.read_sql_query("SELECT * FROM cloc LIMIT 10", con=conn)
conn.close()

print(df)

# plot stats
fig = px.line(df, x="index", y="file_count")
pio.write_image(fig, "test.png", width=800, height=600)
