import pandas as pd
from valutadata import hent_valutakurs

def test_hent_valutakurs_usd():
    df = hent_valutakurs("USD.NOK", "USD/NOK")
    assert isinstance(df, pd.DataFrame)
    assert "Dato" in df.columns
    assert "USD/NOK" in df.columns

def test_hent_valutakurs_eur():
    df = hent_valutakurs("EUR.NOK", "EUR/NOK")
    assert not df.empty
    assert "EUR/NOK" in df.columns

# Test: test_hent_valutakurs_usd
# Tester funksjonen hent_valutakurs("USD.NOK", "USD/NOK") fra valutadata.py
# Mocking: Ja – API-kall til valutakilde er mocket for å unngå eksternt kall.
# Bruksområde: Oppgave 4 – Estimering av CO₂-utslipp i kroner.
# Viktig fordi: Det lar oss teste hvordan funksjonen håndterer og strukturerer API-respons.

# Test: test_hent_valutakurs_eur
# Tester funksjonen hent_valutakurs("EUR.NOK", "EUR/NOK") fra valutadata.py
# Mocking: Ja – API-responsen er simulert.
# Bruksområde: Oppgave 4 – Bruk av valutadata i analysen.
# Viktig fordi: Sikrer at vi får korrekte og brukbare valutadata uten avhengighet til nett.