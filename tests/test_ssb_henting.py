import unittest
from unittest.mock import patch
import pandas as pd
import ssb_henting  # Sørg for at denne ligger i prosjektroten


class TestHentLaksedata(unittest.TestCase):
    """
    Tester for funksjonen hent_laksedata() i ssb_henting.py.
    Formålet er å verifisere at både riktige situasjoner og feilsituasjoner håndteres riktig ved kall for SSB sitt API.
    Dette er relevant for oppgave 2 og 3.
    """

    @patch("ssb_henting.requests.post")
    def test_hent_laksedata_success(self, mock_post):
        """
        Test: test_hent_laksedata_success

        Tester hent_laksedata() fra ssb_henting.py.

        Formålet er å sikre at gyldig data gir en DataFrame med riktig format og innhold.

        Mock brukes for å simulere en vellykket respons fra SSB; oppgave 2 og 3.

        Dette er viktig fordi suksessfulle kall må returnere komplette og brukbare data, som skal kunne brukes videre til analyse og visualisering.
        """

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
        """
        Test: test_hent_laksedata_failure

        Tester feiltilfelle for hent_laksedata().

        Formål:
        Sikre at funksjonen kaster en Exception hvis API feiler,
        f.eks. ved statuskode 500 eller annen feilmelding.

        Mock brukes til å simulere feilrespons fra SSB med statuskode 500.

        Dette er viktig fordi koden må håndtere feil i API på en kontrollert måte; oppgave 2.
        """

        mock_post.return_value.status_code = 500
        mock_post.return_value.text = "Internal Server Error"

        with self.assertRaises(Exception) as context:
            ssb_henting.hent_laksedata()

        self.assertIn("Klarte ikke hente data", str(context.exception))


if __name__ == "__main__":
    unittest.main()

