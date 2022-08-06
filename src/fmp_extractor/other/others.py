# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 07:37:22 2021

@author: sapereira
"""
import pandas as pd
from ..json_extractor import get_jsonparsed_data
from ..config import API_KEY


def extract_gainers():
    """
    Returns top gainers
    Parameters
    -------
    """
    url = f'https://financialmodelingprep.com/api/v3/gainers?apikey={API_KEY}'
    gainers = get_jsonparsed_data(url)
    return gainers


def extract_losers():
    """
    Returns losers of the market
    Parameters
    -------
    """
    url = f'https://financialmodelingprep.com/api/v3/losers?apikey={API_KEY}'
    losers = get_jsonparsed_data(url)
    return losers


def extract_press_releases(ticker: str, limit=10):
    """
    Returns latest press releases for a company
    -------
    Parameters
    -------
    ticker: str
        ticker of the company
    limit: int
        the number of press releases to extract
    Returns
    -------
    dict
    """
    url = f'https://financialmodelingprep.com/api/v3/press-releases/{ticker}?limit={limit}&apikey={API_KEY}'
    pr = get_jsonparsed_data(url)
    return pr


def extract_sec_fillings(ticker,  limit=10):
    """
   Returns latest sec fillings for a company
   -------
   Parameters
   -------
   ticker: list
       list of tickers
   limit: int
       the number of press releases to extract
   Returns
   -------
   dict
   """
    url = f'https://financialmodelingprep.com/api/v3/sec_filings/{ticker}?limit={limit}&apikey={API_KEY}'
    sec = get_jsonparsed_data(url)
    return sec


def extract_list():
    """
    Returns list of all the tickers available
    -------
    pd.DataFrame
    """
    url = f'https://financialmodelingprep.com/api/v3/stock/list?apikey={API_KEY}'
    list_sym = get_jsonparsed_data(url)
    return pd.DataFrame.from_records(list_sym)


def get_profile(ticker):
    """
    Returns the full profile of a company for a given ticker.

    Parameters
    ----------
    ticker : ticker
        The ticker of the company

    Returns
    -------
    df : pd.DataFrame
        The profile as a dataframe
    """
    url = f'https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={API_KEY}'
    list_sym = get_jsonparsed_data(url)
    df = pd.DataFrame.from_records(list_sym)
    return df
