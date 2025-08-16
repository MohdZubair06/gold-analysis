import yfinance as yf

symbol="GC=F"

df = yf.download(symbol, start="2015-01-01")

df.to_csv("gold_data.csv")
print("gold_data.csv saved in the project folder!")
