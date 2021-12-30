import pandas as pd
import numpy as np

# einlesen der Daten
df = pd.read_csv('dataFiles/FinalAnalysisData.csv',
                 sep=",",
                 header=[0],
                 low_memory = False)
#[1 640 688 rows x 12 columns]
#print(df)
# print(df.columns)
# Selection = df[['Material','Order COGS', 'Order Qty']]
Selection = df[['Material','Order Qty']]

# print(Selection)

# analyse der Varianz
Var = df[['Material','Order Qty']].groupby(['Material']).agg([np.mean,np.median,np.var])
Var['coefficent of variation'] = Var[('Order Qty', 'var')] / Var[('Order Qty', 'mean')]
Var['DiffMedianMean'] = abs(Var[('Order Qty', 'median')] - Var[('Order Qty', 'mean')])
print(Var)

Var.to_csv('dataFiles/Analysis/MaterialVarianceOrderQty.csv')