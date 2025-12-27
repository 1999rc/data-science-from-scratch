class TrainingDataGenerator:
    """
    Converts bee memory paths into (X,Y)
    training data,
    """
    def __init__(self,target_x,target_y):
        self.target_x=target_x
        self.target_y=target_y
    def generate(self,path):
        """
        path;list of(x,y)
        returns;X,y
        """
        X=[]
        y=[]
        for i in range(len(path)-1):
            x,y_pos=path[i]
            next_x, _ =path[i+1]
            dx=self.target_x-x 
            dy=self.target_y -y_pos 
            action=next_x-x #-1,0,1 
            X.append([dx,dy])
        return X,y 
        