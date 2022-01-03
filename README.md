# OM2repo 

## order for executing scripts
### main creatoin of analysisDataset
1. main.py
1. insertExistingData.py (execution already done in main.py. Does not need extra execution)
1. VarianzAnalyse.py  (execution already done in main.py. Does not need extra execution)

#### Attention
in dataFiles/Analysis/MaterialVarianceOrderQty.csv, the first 3 lines have to be replaced by:
- Material,mean,median,var,coefficent of variation,DiffMedianMean


### statistical measures and analaysis
- splitByCoefVar.py
- splitByMean.py
- splitByMedian.py
- splitByVarianz.py
