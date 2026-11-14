import pandas as pd
data={
    "name":['Prachi','Neeraj','Samriddhi','bulbul'],
    "salary":[100000,1000000,12000,10000],
    "age":[20,26,23,24]
}
df=pd.DataFrame(data)
print(df)
print("after using drop function")
# df.drop(columns=["age"],inplace=True)
df_row_dropped=df.drop(0)
print(df_row_dropped)