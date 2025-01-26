import yfinance as yf

symbol = 'AAPL'

ticker = yf.Ticker(symbol)

news = ticker.news

for article in news[:5]:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}\n")
