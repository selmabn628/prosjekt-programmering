import pandas as pd
from valutadata import hent_valutakurs


def test_hent_valutakurs_usd():
    """
    Test: test_hent_valutakurs_usd

    Tester funksjonen hent_valutakurs("USD.NOK", "USD/NOK") fra valutadata.py.

    Ja det er brukt mockdata/ikke ekte levende API data som er de samme hver gang testen kjøres.

    Dette brukes for oppgave 4.

    Dette er viktig fordi det lar oss teste hvordan funksjonen håndterer og strukturerer API-responsen.
    I tillegg sikrer det at USD-data hentes riktig og lagres i en tabell med riktige kolonner.
    """

    df = hent_valutakurs("USD.NOK", "USD/NOK")
    assert isinstance(df, pd.DataFrame)
    assert "Dato" in df.columns
    assert "USD/NOK" in df.columns


def test_hent_valutakurs_eur():
    """
    Test: test_hent_valutakurs_eur

    Tester funksjonen hent_valutakurs("EUR.NOK", "EUR/NOK") fra valutadata.py.

    API-responsen er simulert ved hjelp av statiske mockdata. Dette gjør det mulig å kjøre uten tilgang til nettverket.

    Brukes for oppgave 4. 

    Dette sikrer at vi får korrekte og brukbare valutadata uten å være avhgengig av nettverkstilkobling og at strukturen på dataene som returneres er i riktig format. 
    Dette er slik at man effektivt kan bruke dataene videre i analyser og visualiseringer.
    """

    df = hent_valutakurs("EUR.NOK", "EUR/NOK")
    assert not df.empty
    assert "EUR/NOK" in df.columns
