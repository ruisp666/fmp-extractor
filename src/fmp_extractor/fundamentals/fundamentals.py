from ..json_extractor import get_jsonparsed_data
from ..config import API_KEY


def get_income_statement(tickers, period='year'):
    """
    Extracts the historic income statement for a list of tickers
    Parameters
    ----------
    tickers: list
        Contains the tickers
    period: str
        The frequency ('year' or 'quarter')
    -------
    """

    tickers_is = {}
    if not isinstance(tickers, list):
        raise TypeError('function expects a list.')
    for ticker in tickers:
        url = f'https://financialmodelingprep.com/api/v3/income-statement/{ticker}?period={period}&limit=400&apikey' \
              f'={API_KEY} '
        full_info = get_jsonparsed_data(url)
        tickers_is[ticker] = full_info
    return tickers_is


def get_balance_sheet(tickers, period='year'):
    """
    Extracts the historic balance-sheet for a list of tickers
    Parameters
    ----------
    tickers: list
        Contains the tickers
    period: str
        The frequency ('year' or 'quarter')

    Returns
    -------
    dict
    """
    tickers_bs = {}
    for ticker in tickers:
        url = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?period={period}&limit=400' \
              f'&apikey={API_KEY} '
        full_info = get_jsonparsed_data(url)
        tickers_bs[ticker] = full_info
    return tickers_bs


def get_cash_flow(tickers, period='year'):
    """
    Extracts the historic cash-flow statement for a list of tickers
    Parameters
    ----------
    tickers: list
        Contains the tickers
    period: str
        The period('year' or 'quarter')

    Returns
    -------
    dict
    """
    tickers_cf = {}
    for ticker in tickers:
        url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?period={period}&limit=400&apikey' \
              f'={API_KEY} '
        full_info = get_jsonparsed_data(url)
        tickers_cf[ticker] = full_info
    return tickers_cf


def get_enterprise_value(tickers, period='year'):
    """
    Extracts the historic enterprise-value and share-related info for a list of tickers
    Parameters
    ----------
    tickers: list
        Contains the tickers
    period: str
        The period ('year' or 'quarter')
    Returns
    -------
    dict
    """
    tickers_ev = {}
    for ticker in tickers:
        url = f'https://financialmodelingprep.com/api/v3/enterprise-values/{ticker}?period={period}&limit=400&apikey' \
              f'={API_KEY} '
        full_info = get_jsonparsed_data(url)
        tickers_ev[ticker] = full_info
    return tickers_ev
