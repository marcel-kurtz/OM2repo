# merges existing Data, and 0 value dataset from main.py to one DF
# groups data by ['Material', 'Month', 'Year' ] and sums up all values
# -> this gives total sales
#
import os

import pandas as pd
import numpy as np

# einlesen der Daten
df = pd.read_csv('dataFiles/Swarovski.csv',
                 sep=";",
                 header=[0],
                 index_col=0,
                 low_memory = False)
#[1 048 573 rows x 16 columns]
# print(df)

fullDf = pd.read_csv('dataFiles/FullDatasetEmptyValues.csv',
                 sep=",",
                 header=[0],
                 index_col=0,
                 low_memory = False)
#[5 707 752 rows x 16 columns]
# print(fullDf)

crossProd = pd.read_csv('dataFiles/CrossProd.csv',
                 sep=",",
                 header=[0],
                 index_col=0,
                 low_memory = False)

# print(crossProd.columns)
# print(fullDf.columns.difference(crossProd.columns))

# Insert Existing Data
fullDf = fullDf.append(df)

fullDf.to_csv('dataFiles/DataAfterAppend.csv')
print(fullDf.dtypes)
fullDf['Order COGS'].astype('int64', errors='ignore', copy=False)
print(fullDf.columns)
print(fullDf.dtypes)

# TODO: consider different solution for: Item;Productkey;Size;Colour;Foiling;Effect;Lead Time;Month;Year;Day;Date
# sums up all values to get totoal of whole month per Material
# current solution just makes sense for: Order Qty;Order COGS
fullDf = fullDf.groupby(by=['Material', 'Month', 'Year' ]).sum()
print(fullDf.columns)
#[5 707 752 rows x 16 columns]
print(fullDf)
#Save file
fullDf.to_csv('dataFiles/FinalAnalysisData.csv')

# execute insertExistingData.py file
os.system("VarianzAnalyse.py")