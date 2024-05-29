import random
from typing import List

from pandas import DataFrame

DATA: dict[str, List[int]] = {
    "x",
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "y",
    [random.uniform(0, 100) for _ in range(10)],
}

DF: DataFrame = DataFrame()
