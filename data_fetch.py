import pandas as pd
import yfinance as yf
import os
# import baostock as bs

#Fetch and format data to get the dataframe contains the following column:
#[formated_datetime][open][close][high][low]
def read(by,proxy = False,port = ''):
    match by:
        case "test_case":
            df = pd.read_csv('data.csv')
            df['formated_datetime'] = pd.to_datetime(df['timestamp'], format='%d/%m/%y %H:%M', dayfirst=True)
            # df = df.sort_values(by='formated_datetime',ascending=True)
            return df
        case "yf":
            if(proxy):
                proxy = 'http://127.0.0.1:'+port
                os.environ['HTTP_PROXY'] = proxy
                os.environ['HTTPS_PROXY'] = proxy
            #Reset index for x axis
            df = yf.download("AAPL",start="2025-06-17", end="2025-06-18", interval="1m").reset_index().rename(columns={'index':'Datetime'})
            
            #Format
            df = df.rename(columns={'Close':'close','Open':'open','High':'high','Low':'low'})
            df['formated_datetime'] = df['Datetime'].dt.tz_convert(None).dt.strftime("%y/%m/%d %H:%M")
            return df
    #Other options