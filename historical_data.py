import yfinance as yf

symbol = 'AAPL'

data = yf.download(symbol, start='2023-01-01', end='2023-12-31')

print(data.head())
