import requests
import pandas as pd

def hent_valutakurs(valutapar, kolonnenavn):
    url = f"https://data.norges-bank.no/api/data/EXR/B.{valutapar}.SP?format=sdmx-json&startPeriod=2000-01-01&endPeriod=2025-04-08&locale=no"
    response = requests.get(url)
    data = response.json()

    dates = data['data']['structure']['dimensions']['observation'][0]['values']
    series_key = list(data['data']['dataSets'][0]['series'].keys())[0]
    observations = data['data']['dataSets'][0]['series'][series_key]['observations']

    records = []
    for key, val in observations.items():
        date = dates[int(key)]['id']
        rate = val[0]
        records.append((date, rate))

    df = pd.DataFrame(records, columns=["Dato", kolonnenavn])
    df["Dato"] = pd.to_datetime(df["Dato"])
    df[kolonnenavn] = pd.to_numeric(df[kolonnenavn])
    df["Ukedag"] = df["Dato"].dt.weekday
    df = df[df["Ukedag"] == 4].copy()
    return df[["Dato", kolonnenavn]].sort_values("Dato")
