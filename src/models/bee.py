from models.memory import Memory
from models.nn import SimpleNN
from .nn import SimpleNN
class Bee:
    def __init__(self,start_x=0,start_y=0):
        #current position 
        self.x=start_x
        self.y=start_y
        self.memory=Memory()
        self.brain=SimpleNN()
        #self.path_memory=[(self.x,self.y)]
        #journey state
         #+1 -> going out for look honey(searching)
        #-1 -> returning home 
        #self.journey=1
        self.memory.remember(self.x,self.y) 
    def move_to_target(self,target_x,target_y):
        """
        Simple deterministic movement toward target
        """
        while(self.x,self.y)!=(target_x,target_y):
            print("LOOP,",self.x,self.y)
          dx=0
          dy=0
          if self.x < target_x:
            dx=1
          elif self.x > target_x:
            dx=-1 
          if self.y < target_y:
            dy=1 
          elif self.y > target_y:
            dy=-1 
          self.move(dx,dy)
          print("MOVED to",self.x,self.y)
    def move(self,dx,dy):
        self.x+=dx 
        self.y+=dy 
        self.memory.remember(self.x,self.y)
    #def found_honey(self):
    def return_home_path(self):
        """
        Path bee will follow to return
        """
        return self.memory.recall_backward()
        #self.journey=-1 
    '''def return_step(self):
        """
        Move one step back using path memory
        """
        if len (self.path_memory)>1:
            #remove current postion 
            self.path_memory.pop()
            #Go to previous position 
            self.x,self.y=self.path_memory[-1]'''
    def position(self):
        return self.x,self.y 
    def move_using_nn(self,target_x,target_y):
        """
        Bee decides movement using neural network
        """
        dx=target_x-self.x 
        dy=target_y-self.y 
        actionself.brain.forward(dx,dy)
        self.x+=action 
        self.memory.remember(self.x,self.y)
        return action