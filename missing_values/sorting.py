import pandas as pd
data={
    "name":['rahul','tina','manisha'],
    "age":[20,10,9],
    "salary":[123,345,12]

}
df=pd.DataFrame(data)
df.sort_values(by='age',ascending=True,inplace=True)
print(df)