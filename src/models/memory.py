class Memory:
    """
    Stores the path taken by the bee.
    Acts as training data for feature-leaning
    """
    def __init__(self):
        self.path=[]
    def remember(self,x,y):
        """Store current position"""
        self.path.append((x,y))
    def recall_backward(self):
       """
       Return path from last to first(way home)
       """
       return list(reversed(self.path))
    def clear(self):
        """
        Clear memory after reaching hive
        """
        self.path=[]
    def __len__(self):
        return len(self.path)
    def __repr__(self):
        return f"Memory(steps={len(self.path)})"
        