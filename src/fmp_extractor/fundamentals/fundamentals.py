from ..json_extractor import get_jsonparsed_data


def extract_fundamentals_is(tickers, api_key, period='year'):
    """
    Extracts the historic income statement a list of tickers
    Parameters
    ----------
    tickers: list
        Contains the tickers
    api_key: str
    period: str ('year' or 'quarter')

    Returns
    -------
    dict
    """

    tickers_is = {}
    if not isinstance(tickers, list):
        raise TypeError('function expects a list.')
    for ticker in tickers:
        url = f'https://financialmodelingprep.com/api/v3/income-statement/{ticker}?period={period}&limit=400&apikey' \
              f'={api_key} '
        full_info = get_jsonparsed_data(url)
        tickers_is[ticker] = full_info
    return tickers_is


def extract_fundamentals_bs(tickers, api_key, period='year'):
    """
    Extracts the historic balance-sheet for a list of tickers
    Parameters
    ----------
    tickers: list
        Contains the tickers
    api_key: str
    period: str
        The frequency ('year' or 'quarter')

    Returns
    -------
    dict
    """
    tickers_bs = {}
    for ticker in tickers:
        url = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?period={period}&limit=400' \
              f'&apikey={api_key} '
        full_info = get_jsonparsed_data(url)
        tickers_bs[ticker] = full_info
    return tickers_bs


def extract_fundamentals_cf(tickers, api_key, period='year'):
    """
    Extracts the historic cash-flow statement for a list of tickers
    Parameters
    ----------
    tickers: list
        Contains the tickers
    api_key: str
    period: str
     The frequency ('year' or 'quarter')

    Returns
    -------
    dict
    """
    tickers_cf = {}
    for ticker in tickers:
        url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?period={period}&limit=400&apikey' \
              f'={api_key} '
        full_info = get_jsonparsed_data(url)
        tickers_cf[ticker] = full_info
    return tickers_cf


def extract_fundamentals_ev(tickers, api_key, period='year'):
    """
    Extracts the historic enterprise-value and share-related info for a list of tickers
    Parameters
    ----------
    tickers: list
        Contains the tickers
    api_key: str
    period: str
        The frequency ('year' or 'quarter')
    Returns
    -------
    dict
    """
    tickers_ev = {}
    for ticker in tickers:
        url = f'https://financialmodelingprep.com/api/v3/enterprise-values/{ticker}?period={period}&limit=40&apikey' \
              f'={api_key} '
        full_info = get_jsonparsed_data(url)
        tickers_ev[ticker] = full_info
    return tickers_ev
