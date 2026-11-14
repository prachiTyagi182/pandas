import pandas as pd
data={
    "age":[20,30,12,16,19],
    "name":["prachi","sam","sneha","riddhi","bulbul"],
    "salary":[20000,13000,1400,15000,12000],
    "section":["a","b","c","d","e"]
}

df=pd.DataFrame(data)
df.sort_values(by=["age","salary"],ascending=[True,False],inplace=True)
print(df)