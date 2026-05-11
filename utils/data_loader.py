import pandas as pd
from functools import lru_cache

@lru_cache(maxsize=5)
def load_data():

    return pd.read_excel(
        "data/processed/base_finale.xlsx"
    )
