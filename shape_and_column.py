import pandas as pd
data={
    "name":["prachi","rahul","tina","anjali"],
    "rollno":[164,178,103,100],
    "marks":[900,450,890,450],
    "salary":[1000000,24000,45000,23400],
    "performance":[456,56,345,123]
}
df=pd.DataFrame(data)
print("dataframe")
print(df)
print(f'shape {df.shape}')
print(f'column_name{df.columns}')