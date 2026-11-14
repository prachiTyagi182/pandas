import pandas as pd
data={
    "name":['Prachi','Neeraj','Samriddhi','bulbul'],
    "salary":[100000,1000000,12000,10000],
    "age":[20,26,23,24]
}
df=pd.DataFrame(data)
print(df)
# df['bonus']=df['salary']*0.2
df.insert(1,"gender",['female','male','female','female'])
print(df)
# print(df.info())
# print(df.describe())
# print(df.tail(2))