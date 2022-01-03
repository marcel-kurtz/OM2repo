# splits by median and makes graphs based on predefined groups
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

# [28950 rows x 4 columns]
lumpyData = df.loc[df['median'] == 0]
# [6173 rows x 4 columns]
stableData = df.loc[df['median'] != 0].loc[df['median'] < 10000 ]
# [8044 rows x 4 columns]
highPerformanceData = df.loc[df['median'] > 10000]

# SplitsSet = [df, lumpyData,stableData,highPerformanceData]
SplitsSet = [df]

for data in SplitsSet:
    xyz = data.sort_values(by="median")['median']
    xyz.index = range(len(xyz))
    plt.plot(xyz)
    plt.ylabel('median')
    plt.yscale('log', base=10)
    plt.savefig('Figures/VisualSplit/median.png', format='png', transparent=True)
    plt.show()



