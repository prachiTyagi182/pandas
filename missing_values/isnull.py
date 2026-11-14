import pandas as pd
data={
    "name":['Prachi',None,'Neeraj','Samriddhi','bulbul'],
    "salary":[100000,None,1000000,12000,10000],
    "age":[20,26,23,24,None]
}
df=pd.DataFrame(data)
print(df.isnull().sum())