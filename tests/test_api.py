import unittest
import pandas as pd
from unittest.mock import patch
from laks_api_for_unittest import fetch_data, process_data  # Importerer funksjonene


class TestSSBAPI(unittest.TestCase):
    """
    Tester for funksjonene fetch_data() og process_data() fra laks_api_for_unittest.
    Formålet er å sjekke at datainnhenting og databehandling fungerer korrekt,
    med bruk av mocking for å unngå at man er avhengig av eksterne API-er. 
    """

    @patch("laks_api_for_unittest.requests.post")
    def test_fetch_data_success(self, mock_post):
        """
        Test: test_fetch_data_success
        Tester funksjonen fetch_data() fra laks_api_for_unittest.py.
        
        Formål:
        Verifisere at funksjonen returnerer riktig struktur når API-kallet lykkes.

        Mockdata/kuntstig data brukes for å simulere en vellykket respons fra SSB; oppgave 2.

        Viktig fordi:
        Vi tester uten å være avhengig av internett eller eksternt API,
        og sikrer at funksjonen fungerer i kontrollerte forhold.
        """
        mock_response = {
            "dimension": {
                "Tid": {"category": {"label": {"2025U08": "2025U08", "2025U09": "2025U09"}}},
                "VareGrupper2": {"category": {"label": {"Fersk laks": "Fersk laks", "Frosset laks": "Frosset laks"}}},
                "ContentsCode": {"category": {"label": {"Kilospris": "Kilospris", "Vekt (tonn)": "Vekt (tonn)"}}}
            },
            "value": [100, 200, 300, 400, 600, 700, 800]
        }

        # Simulerer en vellykket respons
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response

        data = fetch_data()
        self.assertIsInstance(data, dict)
        self.assertIn("dimension", data)
        self.assertIn("value", data)

    def test_process_data_structure(self):
        """
        Test: test_process_data_structure
        Tester funksjonen process_data() fra laks_api_for_unittest.py.
        
        Formålet er å sikre at JSON-data blir prosessert til en DataFrame med riktig struktur og kolonnenavn.

        Det er brukt statisk mockdata for å simulere API-responsen som er manuelt laget. 
        Testdataene er i JSON-format og er laget for hånd for å ligne den samme strukturen som API-et vanligvis gir tilbake.

        Oppgave 3 handler om strukturering og klargjøring av data.
        Dette er viktig for at man skal kunne visualisere og analysere dataene videre på en effektiv måte.
        
        """
        mock_data = {
            "dimension": {
                "Tid": {"category": {"label": {"2025U08": "2025U08", "2025U09": "2025U09"}}},
                "VareGrupper2": {"category": {"label": {"Fersk laks": "Fersk laks", "Frosset laks": "Frosset laks"}}},
                "ContentsCode": {"category": {"label": {"Kilospris": "Kilospris", "Vekt (tonn)": "Vekt (tonn)"}}}
            },
            "value": [100, 200, 300, 400, 500, 600, 700, 800]
        }

        df = process_data(mock_data)

        # Sjekker at vi fikk en Pandas DataFrame
        self.assertIsInstance(df, pd.DataFrame)

        # Sjekker at de forventede kolonnene finnes
        expected_columns = [
            "År og ukenr.",
            "Fersk laks - Kilospris",
            "Fersk laks - Vekt (tonn)",
            "Frosset laks - Kilospris",
            "Frosset laks - Vekt (tonn)"
        ]
        self.assertListEqual(list(df.columns), expected_columns)


if __name__ == '__main__':
    unittest.main()
