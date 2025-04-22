# fil: tests/test_ssb_henting.py

import unittest
from unittest.mock import patch
import ssb_henting
import pandas as pd

class TestSSBHenting(unittest.TestCase):

    @patch("ssb_henting.requests.post")
    def test_hent_laksedata_success(self, mock_post):
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

    @patch("ssb_henting.requests.post")
    def test_hent_laksedata_failure(self, mock_post):
        mock_post.return_value.status_code = 500
        with self.assertRaises(Exception):
            ssb_henting.hent_laksedata()

if __name__ == '__main__':
    unittest.main()

