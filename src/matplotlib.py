import matplotlib.pyplot as plt
from src import DF

DF.plot.line(x="x-axis", y="y-axis")
plt.ylabel("Y Axis Label")
plt.xlabel("X Axis Label")
plt.title("Example Chart")
plt.tight_layout()
plt.savefig("matplotlib.png")
