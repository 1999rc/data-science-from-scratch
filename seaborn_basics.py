import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
df=pd.read_csv("employees.csv")
df.columns=df.columns.str.strip().str.capitalize()
print(df.columns)
sns.histplot(df["Income"],kde=True)
plt.title("Income Destribution")
plt.savefig("income_destribution.png")
plt.clf()
sns.scatterplot(data=df,x="Age",y="Income",hue="Level")
plt.title("Age vs Income")
plt.savefig("age_vs_income.png")
plt.clf()

