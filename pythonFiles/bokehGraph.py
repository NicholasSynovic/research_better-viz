# importing stuff
import sqlite3

import pandas as pd
from bokeh.plotting import figure, show

# Path to .db file
sql_file_path = "../Example-Data.db"

# Connect to the SQLite database
conn = sqlite3.Connection(database=sql_file_path)
df = pd.read_sql_query("SELECT * FROM cloc LIMIT 10", con=conn)
conn.close()

p = figure()
p.line(x=df["index"], y=df["file_count"], legend_label="Temp.", line_width=2)
print(df)
output_file("line.html")
show(p)
