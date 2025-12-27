class Hive:
    def __init__(self,x=0,y=0):
        """
        Hive has a fixed position.
        it stores honey collected by the bee
        """
        self.x=x 
        self.y=y 
        self.honey_storage=0
    def position(self):
        """Return hive position"""
        return self.x,self.y 
    def store_honey(self,amount=1):
        """Store honey brought by the bee"""
        self.honey_storage+=amount 
    def __repr__(self):
        return f"Hive(x={self.x},y={self.y},
        honey={self.honey_storage})"
        