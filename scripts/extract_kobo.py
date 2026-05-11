import requests
import pandas as pd

TOKEN = "YOUR_TOKEN"
ASSET_ID = "YOUR_ASSET_ID"

url = f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_ID}/data/"

headers = {
    "Authorization": f"Token {TOKEN}"
}

response = requests.get(
    url,
    headers=headers
)

data = response.json()["results"]

df = pd.DataFrame(data)

df.to_excel(
    "data/raw/kobo_raw.xlsx",
    index=False
)

print("Extraction terminée")
