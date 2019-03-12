import pandas as pd
import numpy as np
import glob
from functools import reduce


######## Read data ----------------------------------------

## read ICD2MDC
icd2mdc = pd.read_excel("./data/ICD2MDC.xlsx")
icd2mdc["ICDｺｰﾄﾞ"] = icd2mdc["ICDｺｰﾄﾞ"].apply(lambda x: x[:-1] if "$" in x else x)
icd2mdc = icd2mdc[["ICDｺｰﾄﾞ", "MDC6桁"]]
#icd2mdc.rename(columns={"ICDｺｰﾄﾞ":"ICD10", "MDC6桁":"MDC"}, inplace=True)
dict_icd2mdc = dict(icd2mdc.values)
list_mdc = list(set(dict_icd2mdc.values()))

## read MDC files
files = glob.glob('./data/（９）疾患別手術有無別処置1有無別集計_MDC*_平成28年度*')
res = []
for file in files:
    res.append(pd.read_excel(file))
df = reduce(lambda x,y: pd.concat([x,y], axis=1), res)
df = df.applymap(lambda x: 0 if x=="-" else x)
df = df[4:]




######## Patient counts per MDC -----------------------------

mdc_pt = {}
for i,v in enumerate(df.columns.isin(list_mdc)):
    if v:
        col = df.columns[i]
        mdc_pt[col] = df.iloc[:, i:i+4].sum(axis=1).sum(axis=0)
  

  
  
######## Show resutls: patient counts per MDC, ICD10-MDC -------------------------------
# mdc_pt
"""
MDC: patient_counts
{'010010': 41916.0,
 '010020': 12698.0,
 '010030': 30542.0,
 '010040': 55367.0,
 '010050': 10613.0,
"""

# dict_icd2mdc
"""
ICD10: MDC
{'A00': '150020',
 'A01': '150020',
 'A020': '150020',
 'A021': '180010',
 'A022': '150020',
"""

        
        
        
