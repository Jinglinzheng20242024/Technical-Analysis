import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

def plot_close(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['formated_datetime'], df['close'])
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%y/%m/%d %H:%M"))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.grid(visible=True)
    plt.title('close plot')
    plt.xlabel('time')
    plt.ylabel('price')
    plt.show()

# def plot_open(df):

# def plot_high(df):

# def plot_low(df):

# def plot_candlestick(df):

def stat_param(df:pd.DataFrame):
    price_col = ['open','close','high','low']
    print(df[price_col].describe())