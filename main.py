from src.utils import greet
from src.numpy_basics import numpy_demo
from src.pandas_basics import pandas_demo
from src.matplotlib_basics import matplotlib_demo
from src.seaborn_basics import seaborn_demo
def main():
   message=greet("Learner")
   print(message)

  #run demo
   numpy_demo()
   pandas_demo()
   matplotlib_demo()
   seaborn_demo() 

    
if __name__=='__main__':
    main()
