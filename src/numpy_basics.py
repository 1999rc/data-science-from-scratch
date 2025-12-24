import numpy as np 
import pandas as pd 
data={
    "name":["A","B","C","D"],
    "Age":[23,35,29,42],
    "Salary":[40000,60000,80000,90000],
}
df=pd.DataFrame(data)
print("PANDAS DESCRIBE OUTPUT;")
print(df.describe())
print("\n------------------\n")
#numpy  part 
ages=np.array([23,35,29,42])
salaries=np.array([40000,60000,80000,90000])
print("OPERATIONS")
print("Ages array:",ages)
print("Mean age:",np.mean(ages))
print("Max salary:",np.max(salaries))
#Reshape example 
matrix=salaries.reshape(2,2)
print("\nReshaped salary matrix")
print(matrix)
print("\n-------------------\n")
print("DATAFRAME FILTERING")
#filter:Age > 30
age_filtered=df[df["Age"]>30]
print("\nPeople with Age > 30:")
print(age_filtered)
#Filter salary >=70000
salary_filtered=df[df["Salary"]>70000]
print("\nPeople with Salary >= 70000:")
print(salary_filtered)
combined_filter=df[(df["Age"]>30)&(df["Salary"]>=7000)]
print("\nPeople with Age > 30 AND Salary >= 70000;")
print(combined_filter)
#Axis concept
arr=np.array([
   [10,20,30],
   [40,50,60]
])
#sum of elements
print(np.sum(arr))
print(np.sum(arr,axis=0))
#Row-wise(Axis=1)
print(np.sum(arr,axis=1))
#Min,Max,Mean with axis
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
#with axis 
print(np.max(arr,axis=0)) #column max 
print(np.min(arr,axis=1)) #row min
salary=np.array([40000,60000,80000,90000])
print([(salary >= 6000)&(salary <=85000)])
#
data=np.array([10,25,30,45,60])
print("Mean:",np.mean(data))
print("Max:",np.max(data))
print("Greater sum",np.sum(matrix,axis=0))
ages=np.array([23,35,29,42])
labels=np.where(ages >=30,"Senior","junior")
print(labels)
#
data=np.array([10,20,30])
print(data+5)
import  random 
np.random.seed(42)
rand=np.random.randint(10,100,size=(3,3))
print(rand)
arr=np.array([40,10,60,20])
print(np.sort(arr))
vals=np.array([1,2,2,3,3,3])
np.unique(vals)
print(np.unique(vals,return_counts=True))
#
scores=np.array([45,67,89,34,76])
print("Passed:",scores[scores >=50])
print("Grades:",np.where(scores >=60,"Passed","Fail"))
print("Sorted:",np.sort(scores))

