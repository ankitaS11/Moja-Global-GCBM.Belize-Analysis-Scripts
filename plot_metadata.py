import pandas as pd
import sys

defaults = {
    "path": "output/metadata.csv",
    "label": "Rh"
}

try:
    label = sys.argv[1]
except IndexError:
    label = defaults["label"]

try:
    path = sys.argv[2]
except IndexError:
    path = defaults["path"]

df = pd.read_csv(path)
ax = df[label].plot.line("YEAR") # x-axis
ax.figure.savefig(f'output/{label}.png', dpi=300)