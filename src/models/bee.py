class Bee:
    def __init__(self,start_x=0,start_y=0):
        #current position 
        self.start_x=start_x
        self.start_y=start_y
        self.path_memory=[(self.x,self.y)]
        #journey state
         #+1 -> going out for look honey(searching)
        #-1 -> returning home 
        self.journey=1 
    def move(self,dx,dy):
        """
        Move the bee by (dx,dy)
        """
        self.x=dx 
        self.y=dy
    def found_honey(self):
        """
        Called when finds honey
        Switch journey to return mode
        """
        self.journey=-1 
    def return_step(self):
        """
        Move one step back using path memory
        """
        if len (self.path_memory)>1:
            #remove current postion 
            self.path_memory.pop()
            #Go to previous position 
            self.x,self.y=self.path_memory[-1]
    def position(self):
        return self.x,self.y 
        