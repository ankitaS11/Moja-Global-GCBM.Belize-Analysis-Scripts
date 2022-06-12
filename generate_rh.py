# Load NPP.csv and NEP.csv, make another column for Rh since:
# NEP = NPP - Rh => Rh = NPP - NEP
# Store the final output in "output/metadata.csv" file

import pandas as pd

df_npp = pd.read_csv("output/NPP.csv")
df_nep = pd.read_csv("output/NEP.csv")

df_combined = df_npp.copy()
df_combined["NEP"] = df_nep["NEP"]
df_combined["Rh"] = df_npp["NPP"] - df_nep["NEP"]
df_combined.index = df_npp["YEAR"]
df_combined = df_combined.drop(["YEAR"], axis=1)

df_combined.to_csv("output/metadata.csv")
print("Output file written to output/metadata.csv, now plot by calling plot_metadata.py")