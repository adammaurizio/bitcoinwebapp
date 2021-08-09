import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock price of Bitcoin!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'BTC'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-7-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Open)
st.line_chart(tickerDf.High)
st.line_chart(tickerDf.Low)
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.line_chart(tickerDf.Dividends)

st.write("""

## Author : Adam Maurizio Winata
## Source Ideas : Data Professor Youtube Channel

""")
