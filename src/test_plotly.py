import plotly.express as px
import plotly.io as pio

from src import DF


def main() -> None:
    fig = px.line(DF, x="x", y="y", title="Example Chart")
    pio.write_image(fig, "img/plotly.png", width=800, height=600)


if __name__ == "__main__":
    main()
