import pandas as pd
import data_fetch
import plot

df = data_fetch.read(by='test_case')
plot.plot_close(df)
plot.stat_param(df)
df = data_fetch.read(by='yf',proxy=False)
plot.plot_close(df)
plot.stat_param(df)