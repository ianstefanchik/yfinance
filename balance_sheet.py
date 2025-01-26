import yfinance as yf

symbol = 'AAPL'

ticker = yf.Ticker(symbol)

balance_sheet = ticker.balance_sheet

print(balance_sheet)
