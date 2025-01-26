import yfinance as yf

symbol = 'AAPL'

ticker = yf.Ticker(symbol)

info = ticker.info

print(f"Sector: {info['sector']}")
print(f"Industry: {info['industry']}")
