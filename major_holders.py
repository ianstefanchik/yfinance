import yfinance as yf

symbol = 'AAPL'
ticker = yf.Ticker(symbol)
holders = ticker.major_holders
print(holders)
