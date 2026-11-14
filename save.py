import pandas as pd
# using dictionary:
data={
    "name":["ram","shyam","rahul","tina"],
    "age":[20,30,45,12,],
    "city":["nagpur","indore","ghaziabad","jaipur"]
}
df=pd.DataFrame(data)
print(df)

# # df.to_csv("prachi_created.csv",index=False)
df.to_excel("prachi_crerated.xlsx",index=False)
# # using list:
# data_1=[["prachi",20],["neeraj",29]]
# df1=pd. DataFrame(data_1,columns=["name","age"])
# print(df1)



# #hackerrank
# import pandas as pd
# n=int(input("enter any number:"))
# students=[]
# for i in range(1,n+1):
#     age=int(input("enter age"))
#     name=input("enter name")
#     students.append([name,age])
# df=pd.DataFrame(students,columns=['name','age'])    
# print(df) 
# print(students)   



import pandas as pd
df=pd.read_csv("shopping_trends.csv",encoding='latin1')
print("this is the info of the dataset")
print(df.info())