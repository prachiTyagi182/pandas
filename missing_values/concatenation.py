import pandas as pd
df_1=pd.DataFrame({
    "id":[1,2,3],
    "name":["rahul","tina","anjali"],
    0:["x","5","z"]
})
df_2=pd.DataFrame({
    "id":[4,5,6],
    "name":["meena","vadhu","r"]
})
conc=pd.concat([df_1,df_2],axis=1,ignore_index=True)
print(conc)