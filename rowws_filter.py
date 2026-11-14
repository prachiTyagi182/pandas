import pandas as pd
data={
    "name":["prachi","rahul","tina","anjali"],
    "rollno":[164,178,103,100],
    "marks":[900,450,890,450],
    "age":[20,30,45,56],
    "salary":[1000000,24000,45000,23400]
}
df=pd.DataFrame(data)
# print(df)
# rows=df[df["salary"]>50000]
rows_2=df[(df["salary"]>50000) & (df["age"]>30)]
print(rows_2)
# print(f'dataframe having salary > 50000 {rows}')
# print("dataframe having salary greater than 500000")
# print(rows)