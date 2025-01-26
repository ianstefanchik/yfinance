import yfinance as yf

symbol = 'AAPL'

ticker = yf.Ticker(symbol)

info = ticker.info

print(f"Company Name: {info['longName']}")
print(f"Current Price: {info['regularMarketPrice']} {info['currency']}")
print(f"Market Cap: {info['marketCap']} {info['currency']}")
