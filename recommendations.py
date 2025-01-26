import yfinance as yf

symbol = 'AAPL'

ticker = yf.Ticker(symbol)

recommendations = ticker.recommendations

print(recommendations)
