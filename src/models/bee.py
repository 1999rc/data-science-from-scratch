from .nn import SimpleNN
class Bee:
    def __init__(self,start_x=0,start_y=0):
        #current position 
        self.start_x=start_x
        self.start_y=start_y
        self.memory=Memory()
        self.brain=SimpleNN()
        #self.path_memory=[(self.x,self.y)]
        #journey state
         #+1 -> going out for look honey(searching)
        #-1 -> returning home 
        #self.journey=1
        self.memory.remember(self.x,self.y) 
    def move(self,dx,dy):
        """
        Move the bee by (dx,dy)
        """
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