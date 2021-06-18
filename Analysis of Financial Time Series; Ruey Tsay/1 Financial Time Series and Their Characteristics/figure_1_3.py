import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/m-ibm3dx2608.txt", sep="     ", index_col=0, engine="python")
df = df[[df.columns[1]]]
df.columns = ["simple return"]
df.index = pd.to_datetime(df.index, format="%Y%m%d")
df["log return"] = np.log(1+df["simple return"])

plt.rcParams["figure.figsize"] = [10,4]
figure, axes = plt.subplots(2)
plt.subplots_adjust(hspace=0.4)
figure.suptitle("Value-weighted monthly simple & log return time series", fontsize=12)
axes[0].plot(df["simple return"], linewidth=0.8)
axes[1].plot(df["log return"], linewidth=0.8)
axes[0].set(xlabel="year", ylabel="simple returns")
axes[1].set(xlabel="year", ylabel="log returns")
plt.show()