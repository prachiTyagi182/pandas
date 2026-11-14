import pandas as pd
data={
    "name":['Prachi','Neeraj','Samriddhi','bulbul'],
    "salary":[100000,1000000,12000,10000],
    "age":[20,26,23,24]
}
df=pd.DataFrame(data)
df.loc[2,"salary"] = 13000
df['salary']=df['salary']*1.05
print(df)