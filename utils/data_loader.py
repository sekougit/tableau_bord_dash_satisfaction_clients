import pandas as pd

from functools import lru_cache


@lru_cache(maxsize=5)
def load_data():

    df = pd.read_excel(
        "data/processed/base_finale.xlsx"
    )

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    df["note_globale"] = pd.to_numeric(
        df["note_globale"],
        errors="coerce"
    )

    return df