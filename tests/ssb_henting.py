# fil: ssb_henting.py

import requests
import pandas as pd
from itertools import product

def hent_laksedata():
    api_url = "https://data.ssb.no/api/v0/no/table/03024/"
    query = {
        "query": [],
        "response": {
            "format": "json-stat2"
        }
    }

    response = requests.post(api_url, json=query)

    if response.status_code != 200:
        raise Exception("Klarte ikke hente data fra SSB")

    data = response.json()
    dimension_names = list(data["dimension"].keys())
    values = data["value"]
    dimensions = [list(data["dimension"][dim]["category"]["label"].values()) for dim in dimension_names]
    all_combinations = list(product(*dimensions))

    df = pd.DataFrame(all_combinations, columns=dimension_names)
    df["Value"] = values

    return df
if __name__ == "__main__":
    df = hent_laksedata()
    print(df.head())


