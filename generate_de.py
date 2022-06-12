# Load NPP.csv and NEP.csv, make another column for Rh since:
# NEP = NPP - Rh => Rh = NPP - NEP
# Store the final output in "output/metadata.csv" file

import pandas as pd

df_nbp = pd.read_csv("output/NBP.csv")
df_nep = pd.read_csv("output/NEP.csv")

# DE = NEP - NBP

df_combined = df_nbp.copy()
df_combined["NEP"] = df_nep["NEP"]
df_combined["DE"] = df_nep["NEP"] - df_nbp["NBP"]
df_combined.index = df_nbp["YEAR"]
df_combined = df_combined.drop(["YEAR"], axis=1)

df_combined.to_csv("output/metadata_with_de.csv")
print("Output file written to output/metadata_with_de.csv, now plot by calling plot_metadata.py")