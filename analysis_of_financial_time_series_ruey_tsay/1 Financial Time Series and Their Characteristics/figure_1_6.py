import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import gaussian_kde

df = pd.read_csv("datasets/d-jpus.txt", sep="  ", index_col=0, engine="python")
df.index = [int(date.replace(" ", "")) for date in df.index]
df.index = pd.to_datetime(df.index, format="%Y%m%d")
df.columns = ["Exchange Rate"]
df["daily relative change"] = df["Exchange Rate"].pct_change()

plt.rcParams["figure.figsize"] = [10,4]
figure, axes = plt.subplots(2,1)
plt.subplots_adjust(hspace=0.4)
figure.suptitle("Plots of USD/JPY and the daily relative change")
axes[0].plot(df["Exchange Rate"], linewidth=0.8)
axes[1].plot(df["daily relative change"], linewidth=0.8)
axes[0].set(xlabel="year", ylabel="yens")
axes[1].set(xlabel="year", ylabel="change")
plt.show()
