from src.fmp_extractor.fundamentals.ratios import get_ratios


def test_ratios():
    df = get_ratios(ticker='U', period='year')
    print(df)

