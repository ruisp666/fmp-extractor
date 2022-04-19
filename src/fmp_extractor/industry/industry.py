from ..config import API_KEY
from ..json_extractor import get_jsonparsed_data


def extract_sector_industry(tickers: list) -> dict:
    """
    Extracts industry and sector for a list of tickers
    Parameters
    ----------
    tickers : list
        The list of tickers to extract
    Returns
    -------
    dict
    """
    tickers_info_segments = {}
    print(f'New tickers {tickers}')
    for ticker in tickers:
        url = f'https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={API_KEY}'
        full_info = get_jsonparsed_data(url)[0]
        d = {}
        for field in ['industry', 'sector', 'companyName']:
            d[field] = full_info[field]
        tickers_info_segments[ticker] = d
    return tickers_info_segments
