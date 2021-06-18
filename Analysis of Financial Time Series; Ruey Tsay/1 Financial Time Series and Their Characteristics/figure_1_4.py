import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import gaussian_kde

df = pd.read_csv("datasets/m-ibm3dx2608.txt", sep="     ", index_col=0, engine="python")
df = df[[df.columns[0]]]
df.columns = ["return"]
df.index = pd.to_datetime(df.index, format="%Y%m%d")
df["log return"] = np.log(1+df["return"])

density = gaussian_kde(df["return"])
log_density = gaussian_kde(df["log return"])

x_1 = np.linspace(-0.4,0.6,1000)
x_2 = np.linspace(-0.4,0.4,1000)
plt.rcParams["figure.figsize"] = [10,6]
figure, axes = plt.subplots(1, 2)
figure.suptitle("Empirical and normal densities for monthly simple & log returns of IBM", fontsize=16)
axes[0].set_title("returns")
axes[1].set_title("log returns")
axes[0].set(xlabel ="simple return", ylabel="density")
axes[1].set(xlabel ="log return", ylabel="density")
axes[0].plot(x_1, density(x_1), label="emprical")
axes[0].plot(x_1, stats.norm.pdf(x_1, df["return"].mean(), df["return"].std()), linestyle="dotted", color="blue", label="normal")
axes[1].plot(x_2, log_density(x_2), label="emprical")
axes[1].plot(x_2, stats.norm.pdf(x_2, df["log return"].mean(), df["log return"].std()), linestyle="dotted", color="blue", label="normal")
axes[0].legend()
axes[1].legend()
plt.show()