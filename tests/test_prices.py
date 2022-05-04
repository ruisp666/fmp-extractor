from fmp_extractor.prices.historic import extract_prices_high_frequency


def test_high_freq():
    symbol = 'TWTR'
    df = extract_prices_high_frequency(symbol, '30min').set_index('date').close.to_frame(name=f'{symbol}').asfreq('h')
    assert symbol in df.columns
