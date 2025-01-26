import yfinance as yf

symbol = 'AAPL'

ticker = yf.Ticker(symbol)

splits = ticker.splits

print(splits)
