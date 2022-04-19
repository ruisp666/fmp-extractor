from ..json_extractor import get_jsonparsed_data


def extract_next_earnings(start_date: str, end_date: str, api_key: str):
    """
    Extracts the day of the next earnings report for a list of tickers
    Parameters
    ----------
    start_date: str
    end_date: str
    api_key: str
    Returns
    -------
    full_info: dict
      A dictionary with the earnings calendar
    -------
    """
    url = f'https://financialmodelingprep.com/api/v3/earning_calendar?from={start_date}&to={end_date}&apikey={api_key}'
    full_info = get_jsonparsed_data(url)
    return full_info


def extract_call_transcript(ticker: str, quarter: int, year: int, api_key: str):
    """
    Returns the transcript of a selected company's
    Parameters
    ----------
    ticker: str
        company ticker
    quarter: int
        accounting quarter
    year: int
        accounting year
    api_key: str
        api key
    Returns
    -------
    transcript :str
    """
    url = f'https://financialmodelingprep.com/api/v3/earning_call_transcript/' \
          f'{ticker}?quarter={quarter}&year={year}&apikey={api_key}'
    obj = get_jsonparsed_data(url)
    try:
        transcript = obj[0]['content']
    except IndexError:
        return False
    return transcript
