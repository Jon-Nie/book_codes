import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import gaussian_kde

df_10 = pd.read_csv("datasets/m-gs10.txt", sep="  ", index_col=0, engine="python")
df_10.index = [int(date.replace(" ", "")) for date in df_10.index]
df_10.index = pd.to_datetime(df_10.index, format="%Y%m%d")
df_10.columns = ["10y"]
print(df_10)

df_1 = pd.read_csv("datasets/m-gs1.txt", sep="  ", index_col=0, engine="python")
df_1.index = [int(date.replace(" ", "")) for date in df_1.index]
df_1.index = pd.to_datetime(df_1.index, format="%Y%m%d")
df_1.columns = ["1y"]
print(df_1)

plt.rcParams["figure.figsize"] = [10,7]
figure, axes = plt.subplots(2,1)
figure.suptitle("Plots of 10-year & 1-year treasury rates")
axes[0].plot(df_10["10y"])
axes[1].plot(df_1["1y"])
axes[0].set(xlabel="year", ylabel="10y Rate")
axes[1].set(xlabel="year", ylabel="1y Rate")
plt.show()
