# import pandas as pd
# df_customer=pd.DataFrame({
#     "CustomerID":[1,2,3],
#     "Name":["Ramesh","suresh","rinkesh"]
# })
# df_order=pd.DataFrame({
#     "CustomerID":[1,2,4],
#     "orderAmount":[250,350,400]
# })

# df_merged=pd.merge(df_customer,df_order,on="CustomerID",how="left")
# print("after merging")
# print(df_merged)




import pandas as pd
df_customer=pd.DataFrame({
    "CustomerID":[1,2,3],
    "Name":["Ramesh","suresh","rinkesh"]
})
df_order=pd.DataFrame({
    "CustomerID":[1,2,4],
    "orderAmount":[250,350,400]
})

df_merged=df_customer.merge(df_order,how="cross")
print("after merging")
print(df_merged)