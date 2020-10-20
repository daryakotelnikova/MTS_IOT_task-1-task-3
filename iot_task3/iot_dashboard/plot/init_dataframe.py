import numpy as np
import pandas as pd


def init_dataframe():
    dtypes = np.dtype([
        ("co", np.float),
        ("humidity", np.float),
        ("light", np.bool),
        ("lpg", np.float),
        ("motion", np.bool),
        ("smoke", np.float),
        ("temp", np.float),
        ("device_id", str),
        ("ts", np.float)
    ])
    df = pd.DataFrame(np.empty(0, dtype=dtypes))

    return df
