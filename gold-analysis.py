# Gold Analysis Project 
# Author: Mohd Zubair
# Date: 16 August 2025 📅
# Description: Analyzes historical gold futures prices, computes moving averages, returns, and plots charts.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#===== 1) Load Gold Data =====

cols=['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

df = pd.read_csv(
    "gold_data.csv",
    skiprows=3, 
    names=cols, 
    parse_dates=['Date']
    index_col='Date')
print(df.head())
print("Data loaded:", df.shape)


#===== 2) Clean Data =====

df.fillna(method='ffill', inplace=True)
df.dropna(inplace=True)


#===== 3) Technical Indicators =====

# Moving Average
df['MA_20'] = df['Close'].rolling(20).mean()
df['MA_50'] = df['Close'].rolling(50).mean()
df['MA_200'] = df['Close'].rolling(200).mean()

# Daily Returns
df['Returns'] = df['Close'].pct_change()
df.dropna(inplace=True)

# Cumulative Returns
df['Cumulative'] = (1 + df['Returns']).cumprod()


#===== 4) Plots =====

# Price + Moving Averages
plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Close')
plt.plot(df['MA_20'], label='MA 20')
plt.plot(df['MA_50'], label='MA 50')
plt.plot(df['MA_200'], label='MA 200')
plt.title("Gold Price with Moving Averages")
plt.legend()
plt.savefig("1_price_ma.png")
plt.show()

# Returns Histogram
plt.figure(figsize=(12, 6))
plt.hist(df['Returns'], bins=50)
plt.title("Daily Returns Histogram")
plt.savefig("2_returns_hist.png")
plt.show()

# Cumulative Returns
plt.figure(figsize=(12, 6))
plt.plot(df['Cumulative'])
plt.title("Cumulative Returns of Gold")
plt.savefig("3_cum_return.png")
plt.show()


#===== 5) Summary Stats =====

summary = {
    "Start Date": df.index.min(), 
    "End Date": df.index.max(),
    "Total Return": df['Cumulative'].iloc[-1]-1,
    "Mean Daily Return": df['Returns'].mean(),
    "Volatility (Std)": df['Returns'].std()
}

with open("summary.txt", "w") as f:
    for k, v in summary.items():
        f.write(f"{k}:{v}\n")

print("✅ Analysis complete! Check PNG charts & summary.txt")
