import yfinance as yf

symbol = 'AAPL'
ticker = yf.Ticker(symbol)
institutional_holders = ticker.institutional_holders
print(institutional_holders)
