"""
Koden henter laksedata fra SSB og gjør dataen om til en tabell for alle verdiene som brukes videre i prosjektet ved hjelp av Pandas.
"""

import requests
import pandas as pd
from itertools import product

# URL til SSB API for tabell 03024
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
   

    dimensions = [list(data["dimension"][dim]["category"]["label"].values()) for dim in dimension_names]
    all_combinations = list(product(*dimensions))
    

    df = pd.DataFrame(all_combinations, columns=dimension_names)
    df["Value"] = values  
    

    df_pivot = df.pivot_table(index="Tid", columns=["VareGrupper2", "ContentsCode"], values="Value", aggfunc="sum").reset_index()
    
    
    df_pivot.columns = ["År og ukenr.", "Fersk laks - Kilospris", "Fersk laks - Vekt (tonn)", "Frosset laks - Kilospris", "Frosset laks - Vekt (tonn)"]
    
    return df_pivot

def main():
    """Hovedfunksjon for å hente og prosessere data."""
    try:
        data = fetch_data()
        df_pivot = process_data(data)
        print(df_pivot.to_string(index=False))
        print("Data hentet, sortert og formatert for visning.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()