import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import datetime
from datetime import date
import yfinance as yf
yf.pdr_override()

today = date.today()
fiveYearsAgo = today - datetime.timedelta(days = 5 * 365)
endDate = today
startDate = fiveYearsAgo
tickers = ['SPY', 'QQQ', 'IWM', 'IVV', 'XLF', 'ARKK', 'XLK', 'VEA', 'SMH']

prices = pdr.get_data_yahoo(tickers, start = startDate, end = endDate)

#comment out the below line to remove normalized returns to graph
prices = prices.apply(lambda x: x / x[0])

prices["Adj Close"].dropna(axis='columns').plot(figsize=(20,10))
plt.show()