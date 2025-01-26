import yfinance as yf

symbol = 'AAPL'

ticker = yf.Ticker(symbol)

cash_flow = ticker.cashflow

print(cash_flow)
