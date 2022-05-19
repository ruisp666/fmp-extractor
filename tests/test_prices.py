from src.fmp_extractor.prices.historic import extract_prices_high_frequency, get_price_change_curve
from src.fmp_extractor.prices.live import extract_prices_all_nyse


def test_high_freq():
    symbol = 'TWTR'
    df = extract_prices_high_frequency(symbol, '30min').set_index('date').close.to_frame(name=f'{symbol}').asfreq('h')
    assert symbol in df.columns


def test_all_nyse():
    df = extract_prices_all_nyse()


def test_price_changes():
    df = get_price_change_curve('TWTR')
    assert '10Y' in df.columns