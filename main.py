from src.utils import greet
from src.numpy_basics import numpy_demo
from src.pandas_basics import pandas_demo
from src.matplotlib_basics import matplotlib_demo
from src.seaborn_basics import seaborn_demo
'''
class DemoRunner:

  def __init__(self,name:str,run_plots:bool=False):
     self.name=name
     self.run_plots=run_plots

  def greet_user(self):
   print(gree(self.name))
  def run_demos(self):
   numpy_demo()
   pandas_demo()
   if self.run_plots:
      matplotlib_demo()
      seaborn_demo()
#  def main():
   runner=DemoRunner("Lerner",run_plots=False)
   runner.greet_user()
   runner.run_demos()
        
#if __name__=='__main__':
   # main()
'''
def numpy_demo():
  print("Numpy demo running...!")
numpy_demo()

def matplotlib_demo():
  print("matplotlib demo running...!")
matplotlib_demo()

def pandas_demo():
  print("Pandas demo running...!")
pandas_demo()

def seaborn_demo():
  print("Seaborn demo running...!")
seaborn_demo()

class  DemoRunner:

 def __init__(self,name:str,run_plots:bool=True):
   self.name=name 
   self.run_plots=run_plots
   self.demos={
      "numpy":self.numpy_demo_func,
      "pandas":self.pandas_demo,
      "matplotlib":self.matplotlib_demo,
      "seaborn":self.seaborn_demo,
  }
 def greet_user(self):
    print(greet(self.name))

 def numpy_demo_func(self):
   numpy_demo()

 def pandas_demo(self):
   pandas_demo()

 def matplotlib_demo(self):
   matplotlib_demo()

 def seaborn_demo(self):
   seaborn_demo()

 def run_demos(self,demo_names):
    for name in demo_names:
       if name not in self.demos:
          print(f"Demon not found:{name}")
          continue
          print(f"\nRunning {name} demo")
          self.demos[name]()

def main():
    runner=DemoRunner("Lerner",run_plots=False)
    runner.greet_user()
    runner.run_demos(["numpy","pandas"])

if __name__=='__main__':
    main()
