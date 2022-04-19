# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 07:37:22 2021

@author: sapereira
"""
import pandas as pd
from ..json_extractor import get_jsonparsed_data


# ToDo: Organize the remaining extractors


def extract_gainers(api_key: str):
    """
    Returns top gainers
    Parameters
    -------
    api_key: str
       api key
    Returns
    -------
    dict
    """
    url = f'https://financialmodelingprep.com/api/v3/gainers?apikey={api_key}'
    gainers = get_jsonparsed_data(url)
    return gainers


def extract_losers(api_key: str):
    """
    Returns losers of the market
    Parameters
    -------
    api_key: str
       api key
    Returns
    -------
    dict
    """
    url = f'https://financialmodelingprep.com/api/v3/losers?apikey={api_key}'
    losers = get_jsonparsed_data(url)
    return losers


def extract_press_releases(ticker: str, api_key: str, limit=10):
    """
    Returns latest press releases for a company
    -------
    Parameters
    -------
    ticker: str
        ticker of the company
    api_key: str
        api key
    limit: int
        the number of press releases to extract
    Returns
    -------
    dict
    """
    url = f'https://financialmodelingprep.com/api/v3/press-releases/{ticker}?limit={limit}&apikey={api_key}'
    pr = get_jsonparsed_data(url)
    return pr


def extract_sec_fillings(ticker, api_key: str, limit=10):
    """
   Returns latest sec fillings for a company
   -------
   Parameters
   -------
   ticker: list
       list of tickers
   api_key: str
       api key
   limit: int
       the number of press releases to extract
   Returns
   -------
   dict
   """
    url = f'https://financialmodelingprep.com/api/v3/sec_filings/{ticker}?limit={limit}&apikey={api_key}'
    sec = get_jsonparsed_data(url)
    return sec


def extract_list(api_key: str):
    """
    Returns list of all the tickers available
    -------
    pd.DataFrame
    """
    url = f'https://financialmodelingprep.com/api/v3/stock/list?apikey={api_key}'
    list_sym = get_jsonparsed_data(url)
    return pd.DataFrame.from_records(list_sym)
