import requests
import pandas as pd
from itertools import product

API_URL = "https://data.ssb.no/api/v0/no/table/03024/"

def fetch_data(api_url=API_URL):
    """Henter data fra SSB API og returnerer JSON-responsen."""
    query = {
        "query": [],
        "response": {"format": "json-stat2"}
    }
    response = requests.post(api_url, json=query)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Feil ved henting av data: {response.status_code}\n{response.text}")

def process_data(data):
    """Prosesserer JSON-data og returnerer en formatert Pandas DataFrame."""
    dimension_names = list(data["dimension"].keys())
    values = data["value"]

    # Oppretter en liste av kombinasjoner av dimensjoner
    dimensions = [list(data["dimension"][dim]["category"]["label"].values()) for dim in dimension_names]
    all_combinations = list(product(*dimensions))

    # Lager en DataFrame med riktige dimensjoner
    df = pd.DataFrame(all_combinations, columns=dimension_names)
    df["Value"] = values

    # Pivoterer data for å få ønsket struktur
    df_pivot = df.pivot_table(
        index="Tid",
        columns=["VareGrupper2", "ContentsCode"],
        values="Value",
        aggfunc="sum"
    ).reset_index()

    # Gir kolonnene mer forståelige navn
    df_pivot.columns = ["År og ukenr."] + [
        f"{vare} - {kode}" for vare, kode in df_pivot.columns.tolist()[1:]
    ]

    return df_pivot
