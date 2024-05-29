import random
from typing import List

from pandas import DataFrame

DATA: dict[str, List[int]] = {
    "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "y": [0, 5, 7, 2, 4, 6, 2, 1, 6, 9],
}

DF: DataFrame = DataFrame(data=DATA)
