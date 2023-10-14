import streamlit as st
import yfinance as yf
import datetime
st.title('Welcome to stock market')
ticker=st.text_input('Enter the stock name','AAPL')
#ticker='AAPL'
#start='2019-01-01'
#end='2022-12-31'
cols1,cols2=st.columns(2)
with cols1:
    start=st.date_input('Enter start date',datetime.date(2019,1,1))
with cols2:
    end=st.date_input('Enter end date',datetime.date(2022,12,31))
ticker_data=yf.Ticker(ticker)
ticker_df=ticker_data.history(period='1mo',start=start,end=end)
st.dataframe(ticker_df)
col1,col2=st.columns(2)
with col1:
    st.write('Daily closing price')
    st.line_chart(ticker_df['Close'])
with col2:
    st.write('Daily High price')
    st.line_chart(ticker_df['High'])
