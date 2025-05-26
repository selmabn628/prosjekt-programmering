import unittest
from unittest.mock import patch
import pandas as pd
import ssb_henting  # Sørg for at denne ligger i prosjektroten

class TestHentLaksedata(unittest.TestCase):

    @patch("ssb_henting.requests.post")
    def test_hent_laksedata_success(self, mock_post):
        """Tester at funksjonen returnerer en gyldig DataFrame med riktige kolonner"""

        # Simulert svar fra SSB API
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "dimension": {
                "Tid": {"category": {"label": {"2024U01": "2024U01", "2024U02": "2024U02"}}},
                "VareGrupper2": {"category": {"label": {"Fersk oppalen laks": "Fersk oppalen laks"}}},
                "ContentsCode": {"category": {"label": {"Vekt (tonn)": "Vekt (tonn)"}}}
            },
            "value": [100, 150]
        }

        df = ssb_henting.hent_laksedata()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)
        self.assertIn("Tid", df.columns)
        self.assertIn("Value", df.columns)

    @patch("ssb_henting.requests.post")
    def test_hent_laksedata_failure(self, mock_post):
        """Tester at funksjonen kaster feil ved statuskode != 200"""
        mock_post.return_value.status_code = 500
        mock_post.return_value.text = "Internal Server Error"

        with self.assertRaises(Exception) as context:
            ssb_henting.hent_laksedata()

        self.assertIn("Klarte ikke hente data", str(context.exception))

if __name__ == "__main__":
    unittest.main()

