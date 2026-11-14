import pandas as pd
data={
    "name":['Prachi',None,'Neeraj','Samriddhi','bulbul'],
    "salary":[100000,None,1000000,12000,10000],
    "age":[20,26,23,24,None]
}
df=pd.DataFrame(data)
print(df)
print("after using dropna")
#this will check row
# (df.dropna(subset=["name","salary","age"],inplace=True))
#this will check specific columns
df.dropna(axis=1,subset=[4],inplace=True)
print(df)