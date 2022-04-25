import io
import logging

import pandas as pd
import requests

from fmp_extractor.config import API_KEY
from fmp_extractor.json_extractor import get_jsonparsed_data


def extract_prices_history(tickers: list, start_date: str = '', end_date: str = ''):
    """
    Parameters
    ----------
    :tickers: List
`       List of tickers
    :api_key: str
        Api Key
    :start_date: str
        start date in the format (YYYY-MM-DD)
    :end_date: str
        end date  in the format (YYYY-MM-DD)
    Returns the stock price time series for all the tickers
    -------
    """

    def extract_single_history(ticker, start_date_=start_date, end_date_=end_date):
        logging.info(f"Extracting data for {ticker}...")
        if start_date_ == 'beginning':
            url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?&serietype=line&apikey={API_KEY}'
        else:
            url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?from={start_date_}' \
                  f'&to={end_date_}&apikey={API_KEY}'
        full_info = get_jsonparsed_data(url)
        if not full_info:
            logging.warning(f'Ticker {ticker} not available')
            pass
        else:
            logging.info(f'Data refreshed for {ticker}')
            df_ = pd.DataFrame.from_records(full_info['historical'])
            df_['symbol'] = ticker
            return df_

    # Extract the history for each ticker and concat
    df = pd.concat([extract_single_history(ticker, start_date, end_date) for ticker in tickers])
    df['date'] = pd.to_datetime(df['date'])
    return df.sort_values(by=['symbol', 'date'])


def extract_prices_bulk(date: str):
    """
    Extracts bulk prices for a given date.
    Parameters
    ----------
    date: str
        Date to extract prices
    Returns
    -------
    bulk_prices_df: pd.DataFrame
    """
    url = f'https://financialmodelingprep.com/api/v4/batch-request-end-of-day-prices'
    response = requests.get(url, params={'date': date, 'apikey': API_KEY})
    bulk_prices_df = pd.read_csv(io.BytesIO(response.content), encoding='utf-8')
    return bulk_prices_df


def extract_prices_high_frequency(ticker: str, freq: str):
    """
    Extract Prices at higher frequency than one day for a given ticker.
    -------------
    ticker: str
    freq: str
        One of '1min', '5min', '15min', '30min', '1hour', '4hour'
    return pandas dataframe with OHLC prices and volume
    """
    url = f'https://financialmodelingprep.com/api/v3/historical-chart/{freq}/{ticker}?apikey={API_KEY}'
    full_info = get_jsonparsed_data(url)
    prices = pd.DataFrame.from_records(full_info)
    prices['date'] = pd.to_datetime(prices['date'])
    prices['symbol'] = ticker
    return prices


