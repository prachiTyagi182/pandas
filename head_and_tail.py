import pandas as pd
df=pd.read_csv("shopping_trends_updated.csv",encoding='latin1')
# print("first 10 rows of data using head")
# print(df.head(10))#by default 5
# print("last 10 rows pf data using tail")
# print(df.tail(10))#by default 5

# iloc-specific position,int ke liye df.iloc[0]=first row
# agr humne index ka name rkha hai koi toh we use label df.loc[label]
print(df.info())