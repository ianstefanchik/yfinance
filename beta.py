import yfinance as yf

symbol = 'AAPL'

ticker = yf.Ticker(symbol)

info = ticker.info

print(f"Beta: {info['beta']}")
