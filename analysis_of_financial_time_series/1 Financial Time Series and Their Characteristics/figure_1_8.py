import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import gaussian_kde

df = pd.read_csv("datasets/ m-gm3dx7508.txt", sep="     ", index_col=0, engine="python")
df.index = pd.to_datetime(df.index, format="%Y%m%d")
df = df[[df.columns[0]]]
df.columns = ["GM"]

plt.rcParams["figure.figsize"] = [10,4]
figure, axes = plt.subplots(2,1)
plt.subplots_adjust(hspace=0.4)
figure.suptitle("Plots of GM monthly simple return ACF with and without time-series object")
axes[0].acorr(df["GM"].values, linewidth=0.8)
axes[1].acorr(df["GM"], linewidth=0.8)
axes[0].set(xlabel="ACF", ylabel="ACF", xlim=[-1, 25])
axes[1].set(xlabel="ACF", ylabel="ACF", xlim=[-0.08, 2])
plt.show()