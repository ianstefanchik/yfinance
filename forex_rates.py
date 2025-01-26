import yfinance as yf

symbol = 'EURUSD=X'

data = yf.download(symbol, period='1d', interval='1m')

print(data.tail())
