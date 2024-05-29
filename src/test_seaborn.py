import matplotlib.pyplot as plt
import seaborn as sns

from src import DF


def main() -> None:
    sns.relplot(kind="line", x="x", y="y", data=DF)
    plt.ylabel("Y Axis Label")
    plt.xlabel("X Axis Label")
    plt.title("Example Chart")
    plt.tight_layout()
    plt.savefig("img/seaborn.png")


if __name__ == "__main__":
    main()
