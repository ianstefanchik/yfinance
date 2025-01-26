import yfinance as yf

symbol = 'AAPL'
ticker = yf.Ticker(symbol)
sustainability = ticker.sustainability
print(sustainability)
