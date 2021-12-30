import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# einlesen der Daten
df = pd.read_csv('dataFiles/Analysis/MaterialVarianceOrderQty.csv',
                 sep=",",
                 header=0,
                 low_memory = False)

df.reset_index()

# [28950 rows x 4 columns]
lumpyData = df.loc[df['var'] == 0]
# [6173 rows x 4 columns]
stableData = df.loc[df['var'] != 0].loc[df['var'] < 10000 ]
# [8044 rows x 4 columns]
highPerformanceData = df.loc[df['var'] > 10000]

# SplitsSet = [df, lumpyData,stableData,highPerformanceData]
SplitsSet = [df]

for data in SplitsSet:
    xyz = data.sort_values(by="var")['var']
    xyz.index = range(len(xyz))
    plt.plot(xyz)
    plt.ylabel('var')
    plt.yscale('log', base=10)
    plt.savefig('Figures/VisualSplit/var.png', format='png', transparent=True)
    plt.show()