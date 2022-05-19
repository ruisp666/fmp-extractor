from ..json_extractor import get_jsonparsed_data
from ..config import API_KEY
import pandas as pd


def get_ratios(ticker, period='year'):
    """
    Extracts a list of performance and operational ratios
    Parameters
    ----------
    ticker: str
        Ticker representing the company
    period: str
        The frequency ('year' or 'quarter')

    Returns
    -------
    dict
    """
    url = f'https://financialmodelingprep.com/api/v3/ratios/{ticker}?period={period}&limit=400' \
          f'&apikey={API_KEY} '
    full_info = get_jsonparsed_data(url)
    df = pd.DataFrame(full_info)
    df['date'] = pd.to_datetime(df['date'])
    return df.set_index('date')