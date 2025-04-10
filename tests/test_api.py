import unittest
import pandas as pd
from unittest.mock import patch
from laks_api_for_unittest import fetch_data, process_data  # Importerer funksjonene

class TestSSBAPI(unittest.TestCase):

    @patch("laks_api_for_unittest.requests.post")
    def test_fetch_data_success(self, mock_post):
        """ Tester om API-et returnerer en gyldig JSON-struktur ved å mocke API-kallet """
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
        """ Tester om data blir prosessert korrekt til en Pandas DataFrame """
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
        expected_columns = ["År og ukenr.", "Fersk laks - Kilospris", "Fersk laks - Vekt (tonn)", "Frosset laks - Kilospris", "Frosset laks - Vekt (tonn)"]
        self.assertListEqual(list(df.columns), expected_columns)

if __name__ == '__main__':
    unittest.main()
