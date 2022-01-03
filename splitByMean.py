# splits by mean and makes graphs based on predefined groups
#
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# einlesen der Daten
df = pd.read_csv('dataFiles/Analysis/MaterialVarianceOrderQty.csv',
                 sep=",",
                 header=0,
                 low_memory = False)

df.reset_index()
print(df)

# [28950 rows x 4 columns]
lumpyData = df.loc[df['mean'] == 0]
# [6173 rows x 4 columns]
stableData = df.loc[df['mean'] != 0].loc[df['mean'] < 10000 ]
# [8044 rows x 4 columns]
highPerformanceData = df.loc[df['mean'] > 10000]

# SplitsSet = [df, lumpyData,stableData,highPerformanceData]
SplitsSet = [df]

for data in SplitsSet:
    xyz = data.sort_values(by="mean")['mean']
    xyz.index = range(len(xyz))
    plt.plot(xyz)
    plt.ylabel('mean')
    plt.yscale('log', base=10)
    plt.savefig('Figures/VisualSplit/mean.png', format='png', transparent=True)
    plt.show()
