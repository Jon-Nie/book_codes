import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
import re

securities = ["SP500", "VW", "EW", "IBM", "INTC", "MMM", "MSFT", "C"]
tickers = ["INTC", "MMM", "MSFT", "C"]
np.seterr(divide = "ignore")

# daily returns
# "d-ibm3dx7008.txt" has some bugs with multiple whitespace as separator instead of a single tab, hence the string manipulation first
with open("datasets/d-ibm3dx7008.txt", "r") as file:
	string = file.read()
string = re.sub("([^\s])[\s\t]{2,}([^\s])", r"\1\t\2", string)
df_d = pd.read_csv(StringIO(string), sep="\t", index_col=0, engine="python")
df_d.index = pd.to_datetime(df_d.index, format="%Y%m%d")

df_d.columns = ("IBM", "VW", "EW", "SP500")
for index, file in enumerate(("d-intc7208.txt", "d-3m7008.txt", "d-msft8608.txt", "d-c8608.txt")):
	df_temp = pd.read_csv(f"datasets/{file}", sep="      ", index_col=0, engine="python")
	df_temp.index = pd.to_datetime(df_temp.index, format="%Y%m%d")
	df_temp = df_temp[[df_temp.columns[0]]]
	df_temp.columns = [tickers[index]]
	df_d = df_d.join(df_temp)
df_d = df_d[securities]
df_d_log = np.log(1+df_d)

# monthly returns
df_m = pd.read_csv("datasets/m-ibm3dx2608.txt", sep="     ", index_col=0, engine="python")
df_m.index = pd.to_datetime(df_m.index, format="%Y%m%d")
df_m = df_m[list(df_m.columns)[:4]]
df_m.columns = ("IBM", "VW", "EW", "SP500")
for index, file in enumerate(("m-intc7308.txt", "m-3m4608.txt", "m-msft8608.txt", "m-c8608.txt")):
	df_temp = pd.read_csv(f"datasets/{file}", sep="      ", index_col=0, engine="python")
	df_temp.index = pd.to_datetime(df_temp.index, format="%Y%m%d")
	df_temp = df_temp[[df_temp.columns[0]]]
	df_temp.columns = [tickers[index]]
	df_m = df_m.join(df_temp)
df_m = df_m[securities]
df_m_log = np.log(1+df_m)

print("                                  Standard                Excess                     ")
print("Security   Start   Size    Mean   Deviation   Skewness   Kurtosis   Minimum   Maximum")
print("_____________________________________________________________________________________")
print("                                  Daily Simple Returns (%)                           ")
for name, start, size, mean, std, skew, kurt, min_, max_ in zip(
	securities, 
	[df_d[sec].dropna().index[0].date().strftime("%y/%m/%d") for sec in securities], 
	df_d.count(), 
	df_d.mean()*100, 
	df_d.std()*100, 
	df_d.skew(), 
	df_d.kurt(), 
	df_d.min()*100, 
	df_d.max()*100
	):
	print(f"{name:8}{start:>8}{size:7d}{mean:8.03f}{std:10.3f}{skew:11.2f}{kurt:11.2f}{min_:11.2f}{max_:10.2f}")
print("")
print("                                  Daily Log Returns (%)                                 ")
for name, start, size, mean, std, skew, kurt, min_, max_ in zip(
	securities,
	[df_d_log[sec].dropna().index[0].date().strftime("%y/%m/%d") for sec in securities], 
	df_d_log.count(), 
	df_d_log.mean()*100, 
	df_d_log.std()*100, 
	df_d_log.skew(), 
	df_d_log.kurt(), 
	df_d_log.min()*100, 
	df_d_log.max()*100
	):
	print(f"{name:8}{start:>8}{size:7d}{mean:8.03f}{std:10.3f}{skew:11.2f}{kurt:11.2f}{min_:11.2f}{max_:10.2f}")
print("")
print("                                  Monthly Simple Returns (%)                         ")
for name, start, size, mean, std, skew, kurt, min_, max_ in zip(
	securities,
	[df_m[sec].dropna().index[0].date().strftime("%y/%m") for sec in securities], 
	df_m.count(), 
	df_m.mean()*100, 
	df_m.std()*100, 
	df_m.skew(), 
	df_m.kurt(), 
	df_m.min()*100, 
	df_m.max()*100
	):
	print(f"{name:8}{start:>8}{size:7d}{mean:8.02f}{std:10.2f}{skew:11.2f}{kurt:11.2f}{min_:11.2f}{max_:10.2f}")
print("")
print("                                   Monthly Log Returns (%)                            ")
for name, start, size, mean, std, skew, kurt, min_, max_ in zip(
	securities,
	[df_m_log[sec].dropna().index[0].date().strftime("%y/%m") for sec in securities], 
	df_m_log.count(), 
	df_m_log.mean()*100, 
	df_m_log.std()*100, 
	df_m_log.skew(), 
	df_m_log.kurt(), 
	df_m_log.min()*100, 
	df_m_log.max()*100
	):
	print(f"{name:8}{start:>8}{size:7d}{mean:8.02f}{std:10.2f}{skew:11.2f}{kurt:11.2f}{min_:11.2f}{max_:10.2f}")
print("_____________________________________________________________________________________")