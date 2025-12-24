import numpy as np 
import pandas as pd 
data={
    "name":["A","B","C","D"],
    "Age":[23,35,29,42],
    "Salary":[40000,60000,80000,90000],
}
df=pd.DataFrame(data)
df.describe()
