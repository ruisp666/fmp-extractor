from datetime import datetime
import pandas as pd
from ..config import API_KEY, API_URL
from ..json_extractor import get_jsonparsed_data


def extract_prices_live(tickers):
    """
    Parameters
    ----------
    tickers: list or set
        The list of tickers
    Returns the stock price time series for all the tickers
    -------
    """

    def extract_price_live_(ticker):
        url = f'https://financialmodelingprep.com/api/v3/quote-short/{ticker}?apikey={API_KEY}'
        full_info = get_jsonparsed_data(url)[0]
        full_info['datetime'] = datetime.now()
        return full_info

    ar = [extract_price_live_(ticker) for ticker in tickers]
    df = pd.DataFrame.from_records(ar)
    return df


def extract_prices_batch(tickers: list, api_key: str = API_KEY):
    """
    Extracts batch quotes.
    Parameters
    ----------
    tickers: list
        List of tickers
    api_key: str
        They Api Key
    Returns
    -------
    batch_prices_df: pd.DataFrame
    """
    str_tickers_ = ','.join(tickers)
    url = f'{API_URL}v3/quote/{str_tickers_}?apikey={api_key}'
    full_info = get_jsonparsed_data(url)
    full_info_df = pd.DataFrame.from_records(full_info)
    full_info_df['timestamp'] = pd.to_datetime(full_info_df['timestamp'], unit='s')
    return full_info_df


if __name__ == '__main__':
    str_tickers = ['TWTR', 'NVDA']
    turn = extract_prices_batch(str_tickers)
    print(turn.columns)
    print(turn.head(5))
