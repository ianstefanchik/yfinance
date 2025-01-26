import yfinance as yf

symbol = 'BTC-USD'

ticker = yf.Ticker(symbol)

info = ticker.info

print(f"Name: {info['name']}")
print(f"Current Price: {info['regularMarketPrice']} {info['currency']}")
print(f"Market Cap: {info['marketCap']} {info['currency']}")
