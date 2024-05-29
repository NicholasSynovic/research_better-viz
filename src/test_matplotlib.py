from matplotlib import pyplot as plt

from src import DF


def main() -> None:
    DF.plot.line(x="x", y="y")

    plt.ylabel("Y Axis Label")
    plt.xlabel("X Axis Label")
    plt.title("Example Chart")
    plt.tight_layout()
    plt.savefig("img/matplotlib.png")


if __name__ == "__main__":
    main()
