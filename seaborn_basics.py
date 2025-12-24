import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
df=pd.read_csv("employees.csv")
df.columns=df.columns.str.strip().str.capitalize()
df=df.rename(columns={"Income":"Salary"})
print(df.columns)
sns.histplot(df["Salary"],kde=True)
plt.title("Salary Destribution")
plt.savefig("income_destribution.png")
plt.clf()
sns.scatterplot(data=df,x="Age",y="Salary",hue="Level")
plt.title("Age vs Salary")
plt.savefig("age_vs_income.png")
plt.clf()

