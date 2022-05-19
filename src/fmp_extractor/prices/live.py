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


def extract_prices_batch(tickers: list):
    """
    Extracts batch quotes.
    Parameters
    ----------
    tickers: list
        List of tickers
    Returns
    -------
    batch_prices_df: pd.DataFrame
    """
    str_tickers_ = ','.join(tickers)
    url = f'{API_URL}v3/quote/{str_tickers_}?apikey={API_KEY}'
    full_info = get_jsonparsed_data(url)
    full_info_df = pd.DataFrame.from_records(full_info)
    full_info_df['timestamp'] = pd.to_datetime(full_info_df['timestamp'], unit='s')
    return full_info_df


def extract_prices_all_nyse():
    """
    Extracts latest snapshot of all stocks traded in nyse.
    --------------------
    Example
       {
      "symbol" : "GSL",
      "name" : "Global Ship Lease, Inc.",
      "price" : 23.73000000,
      "changesPercentage" : 5.41981030,
      "change" : 1.21999930,
      "dayLow" : 22.50000000,
      "dayHigh" : 23.82000000,
      "yearHigh" : 30.02000000,
      "yearLow" : 14.33000000,
      "marketCap" : 875907520.00000000,
      "priceAvg50" : 26.21860000,
      "priceAvg200" : 23.45430000,
      "volume" : 925819,
      "avgVolume" : 1288331,
      "exchange" : "NYSE",
      "open" : 22.50000000,
      "previousClose" : 22.51000000,
      "eps" : 4.60000000,
      "pe" : 5.15869570,
      "earningsAnnouncement" : "2022-05-09T12:30:00.000+0000",
      "sharesOutstanding" : 36911400,
      "timestamp" : 1651648804
    }
    """
    url = f'{API_URL}v3/quotes/nyse?apikey={API_KEY}'
    full_info = get_jsonparsed_data(url)
    full_info_df = pd.DataFrame.from_records(full_info)
    full_info_df['timestamp'] = pd.to_datetime(full_info_df['timestamp'], unit='s')
    full_info_df['earningsAnnouncement'] = pd.to_datetime(full_info_df['earningsAnnouncement'], format="%Y-%m-%dT%H:%M")
    return full_info_df


