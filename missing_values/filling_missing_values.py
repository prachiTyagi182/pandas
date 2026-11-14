# import pandas as pd
# data={
#     "name":['Prachi',None,'Neeraj','Samriddhi','bulbul'],
#     "salary":[100000,None,1000000,12000,10000],
#     "age":[20,26,23,24,None]
# }
# df=pd.DataFrame(data)
# new_data={
#     "name":"meenakshi",
#     "salary":30000,
#     "age":56
# }
# df.fillna(value=new_data,inplace=True)
# print(df)



# import pandas as pd
# data={
#     "name":['Prachi',None,'Neeraj','Samriddhi',None,'bulbul']
# }
# df=pd.DataFrame(data)
# new_name=['Meenakshi','Tina']

# df.loc[df['name'].isnull(),'name']=new_name
# print(df)




import pandas as pd
data={
    "name":['Prachi',None,'Neeraj','Samriddhi','bulbul',None],
    "salary":[100000,None,1000000,12000,10000,None],
    "age":[20,None,26,23,24,None]
}
df=pd.DataFrame(data)
new_data={
    "new_name":['meenakshi','tina'],
    "new_salary":[25000,34000],
    "new_age":[67,45]
}    
df_2=pd.DataFrame(new_data)
df.loc[df['name'].isnull(),['name','salary','age']]=df_2.values
print(df)
