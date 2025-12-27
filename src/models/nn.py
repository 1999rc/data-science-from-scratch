class SimpleNN:
    """
    minimal neural-network scaffold for Bee
    nevigation 
    input :(dx,dy)
    output :action in {-1,0,1}
    """
    def __init__(self,dx,dy):
        """
        Forward pass (no learning yet)
        """
        z=self.w1*dx+self.w2*dy+self.bias 
        return self._activation(z)
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
        