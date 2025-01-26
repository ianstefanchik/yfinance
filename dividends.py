import yfinance as yf

symbol = 'AAPL'

ticker = yf.Ticker(symbol)

dividends = ticker.dividends

print(dividends)
