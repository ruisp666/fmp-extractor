import logging

from ..json_extractor import get_jsonparsed_data

# Set the logging level
logging.getLogger().setLevel(logging.INFO)


def extract_top_news(tickers, api_key: str, limit=15):
    """
    Extracts news for a list of tickers
    Parameters
    ----------
    tickers: list
        Contains the tickers
    api_key: str
    limit: int
        The maximum number of news
    Returns
    -------
    dict
    """
    # Treat the single ticker case in case a string is input
    if isinstance(tickers, str):
        tickers = [tickers]
    tickers_news = {}
    for ticker in tickers:
        url = f'https://financialmodelingprep.com/api/v3/stock_news?tickers={ticker}&limit={limit}&apikey={api_key}'
        full_info = get_jsonparsed_data(url)
        tickers_news[ticker] = full_info
    return tickers_news


def prettify_news(list_news: list, no_print=None):
    """
    Prints news given in a list of dictionaries in a readable way
    Parameters
    ----------
    list_news: list
        Contains the list of dictionaries
    no_print: list
        Arguments to be silenced when printing news.
    """
    if no_print is None:
        no_print = ['image', 'symbol', 'site']
    symbol = list_news[0]['symbol']
    print(f'\n\n\n Latest {len(list_news)} news articles for {symbol}')
    for n in list_news:
        print('*' * 100)
        for topic, content in n.items():
            if topic not in no_print:
                print(f'{topic}: {content}')
