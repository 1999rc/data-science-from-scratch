import pandas as pd 
def pandas_demo():

  data={
   "Name":["A","B","C","D"],
   "Age":[23,35,29,42],
   "Salary":[40000,60000,80000,90000]
  }
  df=pd.DataFrame(data)
  print(df)
  print(df["Age"])
  print(df.info())
  print(df.describe())
  print(df.shape)
  print(df.columns)
  #label based
  #print(df.loc[0])         #row 0
  #print(df.loc[0,"Salary"] # specific value
  #df.loc[df["Age"]>30]
  #position based
  print(df.iloc[0]) #first row 
  print(df.iloc[:,1]) #Age column
  print(df.iloc[1:3,0:2])

  #filtering & conditioning 
  df[df["Age"]>30]
  print(df[df["Salary"]>7000])
  print(df[(df["Age"]>30)&(df["Salary"]>=70000)])
  #modify columns 
  df["Tax"]=df["Salary"]*0.10
  df["Level"]=df["Age"].apply(lambda x:"Senior"if x >=30 else "junior")
  #Missing values 
  df.isna()
  #print(df.dropna())
  df.fillna(0)
  ####
  df=pd.DataFrame({
  "Name":["A","B","C","D"],
  "Age":[23,35,29,42],
  "Salary":[40000,60000,80000,90000]
  })
  df["Bonus"]=df["Salary"]*0.05
  print(df[df["Age"]>30])
  print(df[["Name","Salary"]])
  print(df.loc[df["Salary"] >=70000,["Name","Salary"]])
  print(df.sort_values(by="Salary",ascending=False))
  df.groupby("Age")["Salary"].mean()
  df["Level"]=df["Age"].apply(lambda x:"Senior"if x >= 30 else "junior")
  print(df.groupby("Level")["Salary"].mean())
  df.rename(columns={"Salary":"income"},inplace=True)
  df.drop(columns=["Bonus"])
  df.drop(index=0)

  df.to_csv("employees.csv",index=False)
  pd.read_csv("employees.csv")
  ###
  df=pd.DataFrame({
   "Name":["A","B","C","D"],
   "Age":[25,35,29,42],
   "Salary":[40000,60000,80000,90000]
  })
  df["Level"]=df["Age"].apply(lambda x:"Senior" if x >=30 else "junior")
  print(df.sort_values(by="Salary",ascending=False))
  print(df.groupby("Level")["Salary"].mean())
if __name__=='__main__':
  pandas_demo()
