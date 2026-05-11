import pandas as pd

df = pd.read_excel(
    "data/processed/base_finale.xlsx"
)

# Exemple transformation

df.columns = df.columns.str.lower()

df.to_excel(
    "data/processed/base_finale.xlsx",
    index=False
)

print("Transformation terminée")
