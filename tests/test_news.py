from fmp_extractor.news.news import extract_top_news
import pandas as pd


def test_top_news():
    symbol = 'NFLX'
    n_news = 15
    news = extract_top_news(['NFLX'], limit=n_news)
    df = pd.DataFrame.from_records(list(news.values())[0])
    df['Date'] = df['publishedDate'].str.strip()[:11]
    df['Time'] = df['publishedDate'].str.strip()[11:]
    print(df[['Date', 'Time']])