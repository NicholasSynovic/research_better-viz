# importing stuff
import sqlite3

import pandas as pd
from bokeh.io import export_png, output_notebook
from bokeh.plotting import figure, save, show

# Path to .db file
sql_file_path = "../Example-Data.db"

# Connect to the SQLite database
conn = sqlite3.Connection(database=sql_file_path)
# dfx = pd.read_sql_query("SELECT index FROM cloc LIMIT 10", con=conn)
# dfy = pd.read_sql_query("SELECT file_count FROM cloc LIMIT 10", con=conn)
df = pd.read_sql_query("SELECT * FROM cloc LIMIT 10", con=conn)
conn.close()

x = df.index.to_list()
y = df["file_count"].to_list()

print(df)
p = figure()
p.line(x=x, y=y, legend_label="Temp.", line_width=2)
export_png(p, filename="test.png")
