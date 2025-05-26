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

