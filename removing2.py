import numpy as np
import pandas as pd
data={
    "name":['Prachi','Neeraj','Samriddhi','bulbul'],
    "salary":[100000,1000000,12000,10000],
    "age":[20,26,23,24]
}
df=pd.DataFrame(data)
df.loc[0,["age","salary"]]=np.nan
print(df.fillna(""))