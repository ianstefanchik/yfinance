import yfinance as yf

symbol = 'AAPL'

ticker = yf.Ticker(symbol)

options = ticker.options

print(options)
