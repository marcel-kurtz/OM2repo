import pandas as pd
import numpy as np
# einlesen der Daten
df = pd.read_csv('dataFiles/Swarovski.csv',
                 sep=";",
                 header=[0],
                 index_col=0,
                 low_memory = False)
df2 = df.copy()
# [1 048 573 rows x 16 columns]
print(df)
# Set Col Label
print(df.columns)
columns = df.columns
dtype = df.dtypes


# Name: Cal. year / month, Length: 38, dtype: float64
setMonthYear = df[['Month', 'Year']].drop_duplicates()
# print(setMonthYear)
# print(len(setMonthYear))

# Name: Material, Length: 43176, dtype: int64
setMaterial = df['Material'].drop_duplicates()
# print(setMaterial)

# leadtime adds more combinations [150204 rows x 8 columns]
setMaterialPlus = df[['Material', 'Item','Productkey', 'Size', 'Colour', 'Foiling', 'Effect', 'Lead Time',]].drop_duplicates()
# print(setMaterialPlus)

# [43176 rows x 7 columns]
setMaterialNoLeadtime = df[['Material', 'Item','Productkey', 'Size', 'Colour', 'Foiling', 'Effect']].drop_duplicates()
# print(setMaterialNoLeadtime)

# print(df)

# ERstellen komplettes Gitter auf MOntasbasis mit 0 WErten für
# jede Kombination aus
crossProd = setMaterialPlus.merge(setMonthYear, how='cross')
crossProd.to_csv('dataFiles/CrossProd.csv')
# print(crossProd)

arrayofNANLenOfCrossProd = [np.nan for x in range(len(crossProd))]
missingColumns = columns.difference(crossProd.columns)

# erstellen von vollem dataframe mit allen werten neue Spalten werden mit
fullDf = crossProd.copy()
for Col in missingColumns:
    fullDf[Col] = arrayofNANLenOfCrossProd

#[5707752 rows x 16 columns]
print(fullDf)
fullDf.to_csv('dataFiles/FullDatasetEmptyValues.csv')
