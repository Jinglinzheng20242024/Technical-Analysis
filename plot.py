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
    price_col = ['open', 'close','high','low']
    stats = df[price_col].describe()

    #Add mode, variance, skewness, kurtosis
    stats.loc['mode'] = df[price_col].apply(lambda x: x.mode().tolist())
    stats.loc['variance'] = df[price_col].var()
    stats.loc['skewness'] = df[price_col].skew()
    stats.loc['kurtosis'] = df[price_col].kurtosis()

    print(stats)
