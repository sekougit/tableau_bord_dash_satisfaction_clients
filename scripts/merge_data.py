# import pandas as pd

# clients = pd.read_excel(
#     "data/raw/clients.xlsx"
# )

# kobo = pd.read_excel(
#     "data/raw/kobo_raw.xlsx"
# )

# def clean_phone(x):

#     if pd.isna(x):
#         return None

#     x = str(x)

#     x = x.replace(" ", "")
#     x = x.replace("+221", "")
#     x = x.replace("-", "")

#     return x

# clients["numero"] = (
#     clients["numero"]
#     .apply(clean_phone)
# )

# kobo["numero_telephone"] = (
#     kobo["numero_telephone"]
#     .apply(clean_phone)
# )

# df = clients.merge(
#     kobo,
#     left_on="numero",
#     right_on="numero_telephone",
#     how="left"
# )

# df.to_excel(
#     "data/processed/base_finale.xlsx",
#     index=False
# )

# print("Jointure terminée")
