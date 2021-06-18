import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bond_maturities = ["12", "24", "36", "48", "60", "120"]
bonds = pd.read_csv("datasets/m-fama-bonds.txt", sep="     ", index_col=0, engine="python")
bonds.columns = bond_maturities
bonds.index = pd.to_datetime(bonds.index, format="%Y%m%d")

treasuries_m = pd.DataFrame()
treasury_maturities_m = ["1", "3", "5", "10"]
for maturity in treasury_maturities_m:
	try:
		temp_df = pd.read_csv(f"datasets/m-gs{maturity}.txt", sep="  ", index_col=0, engine="python")
	except:
		temp_df = pd.read_csv(f"datasets/ m-gs{maturity}.txt", sep="  ", index_col=0, engine="python")
	temp_df.index = [int(date.replace(" ", "")) for date in temp_df.index]
	temp_df.index = pd.to_datetime(temp_df.index, format="%Y%m%d")
	temp_df.columns = [maturity]
	treasuries_m[maturity] = temp_df[maturity]

treasuries_w = pd.DataFrame()
treasury_maturities_w = ["3", "6"]
for maturity in treasury_maturities_w:
	temp_df = pd.read_csv(f"datasets/w-tb{maturity}ms.txt", sep="  ", index_col=0, engine="python")
	temp_df.index = [int(date.replace(" ", "")) for date in temp_df.index]
	temp_df.index = pd.to_datetime(temp_df.index, format="%Y%m%d")
	temp_df.columns = [maturity]
	treasuries_w[maturity] = temp_df[maturity]

print("     Descriptive statistics of selected U.S financial time series    ")
print("_____________________________________________________________________")
print("                  Standard                Excess                     ")
print("Maturity   Mean   Deviation   Skewness   Kurtosis   Minimum   Maximum")
print("_____________________________________________________________________")
print("        Monthly Bond Returns: Jan. 1952 to Dec. 2008, T = 684        ")
for name, mean, std, skew, kurt, min_, max_ in zip(
	bond_maturities, 
	bonds.mean()*100, 
	bonds.std()*100, 
	bonds.skew(), 
	bonds.kurt(), 
	bonds.min()*100, 
	bonds.max()*100
	):
	print(f"{name:8}{mean:8.02f}{std:10.2f}{skew:11.2f}{kurt:11.2f}{min_:11.2f}{max_:10.2f}")
print("")

print("     Monthly Treasury Rates: April 1953 to February 2009, T = 671     ")
for name, mean, std, skew, kurt, min_, max_ in zip(
	treasury_maturities_m, 
	treasuries_m.mean(), 
	treasuries_m.std(), 
	treasuries_m.skew(), 
	treasuries_m.kurt(), 
	treasuries_m.min(),
	treasuries_m.max()
	):
	print(f"{name:8}{mean:8.02f}{std:10.2f}{skew:11.2f}{kurt:11.2f}{min_:11.2f}{max_:10.2f}")
print("")

print("          Weekly Treasury Bill Rates: End on March 27, 2009.          ")
for name, mean, std, skew, kurt, min_, max_ in zip(
	treasury_maturities_w, 
	treasuries_w.mean(), 
	treasuries_w.std(), 
	treasuries_w.skew(), 
	treasuries_w.kurt(), 
	treasuries_w.min(), 
	treasuries_w.max()
	):
	print(f"{name:8}{mean:8.02f}{std:10.2f}{skew:11.2f}{kurt:11.2f}{min_:11.2f}{max_:10.2f}")
print("_____________________________________________________________________")