class SimpleNN:
    """
    Very simple neural network unit that leans to move left/
    stay/right
    based on distance from target
    """
    def __init__(self,lr=0.1):
        self.w_dx=0.0
        self.w_dy=0.0
        self.bias=0.0
        self.lr=lr 
    def forward(self,dx,dy):
        z=self.w_dx*dx+self.w_dy*dy+self.bias
        if z > 0.5:
            return 1
        elif z < -0.5:
            return -1 
        else:
            return 0 
    def train(self,X,y,epochs=10):
        """
        X;[[dx,dy],...]
        y;[-1,0,1,...]
        """
        for epoch in range(epochs):
            total_error=0
            for(dx,dy),target in zip(X,y):
                z=self.w_dx*dx+self.w_dy*dy+self.bias
                #prediction raw
                pred=z 
                error=reward(target-pred) 
                total_error+=abs(error)
                #gradient descent update 
                self.w_dx+=self.lr*error*dx 
                self.w_dy+=self.lr*error*dy 
                self.bias+=self.lr*error
            print(f"Epochs {epoch+1},Error;{total_error:,3}")
    '''def __init__(self,dx,dy):
        """
        Forward pass (no learning yet)
        """
        z=self.w1*dx+self.w2*dy+self.bias 
        return self._activation(z)'''
    def _activation(self,z):
        """
        Discrete action selector 
        """
        if z > 0.5:
            return 1 
        elif z < -0.5:
            return -1 
        else:
            return 0 
    def __repr__(self):
        return (
            f"SimpleNN(w1={self.w1},"
            f"w2={self.w2},bias={self.bias}"
            )
#in python >>
'''
after bee finishing journey 
generator=TrainDataGenerator(target_x=0,
target_y=0)
X,y=generator.generate(bee.memory.path)
bee.brain.train(X,y,epochs=20)
'''       