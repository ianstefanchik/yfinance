import yfinance as yf

symbol = 'AAPL'

ticker = yf.Ticker(symbol)

income_statement = ticker.financials

print(income_statement)
