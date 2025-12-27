class RewardSystem:
    """
    Computes reward for bee actions 
    """
    def __init__(self,target_x,target_y):
        self.target_x=target_x
        self.target_y=target_y
    def distance(self,x,y):
        return abs(self.target_x-x)+abs(self.target_y-y)
    def compute(self,prev_pos,new_pos,reached_target=False):
        """
        prev_pos;(x,y)
        new_pos;(x,y)
        """
        if reached_target:
            return 10 
        prev_dist=self.distance(*prev_pos)
        new_dist=self.distance(*new_pos)
        if new_dist < prev_dist:
            return 1 
        else:
            return -1 