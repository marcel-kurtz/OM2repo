# splits by coefficent of variation and makes graphs based on predefined groups
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
lumpyData = df.loc[df['coefficent of variation'] == 0]
# [6173 rows x 4 columns]
stableData = df.loc[df['coefficent of variation'] != 0].loc[df['coefficent of variation'] < 10000 ]
# [8044 rows x 4 columns]
highPerformanceData = df.loc[df['coefficent of variation'] > 10000]

SplitsSet = ['df']# , 'lumpyData','stableData','highPerformanceData']
VariableSet = ['coefficent of variation', 'var', 'mean', 'median', 'DiffMedianMean']
# use local varivale name (as str) as real variable locals()[str]
# SplitsSet = [df]

for data in SplitsSet:
    for varialbe in VariableSet:
        xyz = locals()[data].sort_values(by=varialbe)[varialbe]
        xyz.index = range(len(xyz))
        plt.plot(xyz)
        plt.ylabel(varialbe)
        plt.yscale('log', base=10)
        plt.savefig('Figures/VisualSplit/'+ data +' with '+ varialbe +'.png', format='png', transparent=True)
        plt.clf()



