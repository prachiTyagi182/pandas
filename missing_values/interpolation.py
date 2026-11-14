import pandas as pd
#dictionary creation
data={
    "name":['ram','shyam','rahul','tina'],
    "age":[10,None,20,None]   
}
# data to dataframe
df=pd.DataFrame(data)
print(df)
#fill none value using interpolation
df['age']=df['age'].interpolate(method='linear',axis=0,inplace=True)
print(df)