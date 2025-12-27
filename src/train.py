from models.reward import RewardSystem
from models.data_generator import TrainingDataGenerator
from models.bee import Bee 
bee=Bee(start_x=5,start_y=0)
bee.move_to_target(target_x=0,target_y=0)

reward_system=RewardSystem(target_x=0,target_y=0)
rewards=[]
path=bee.memory.path 
for i in range(len(path)-1):
    r=reward_system.compute(
        prev_pos=path[i],
        new_pos=path[i+1],
        reached_target=(path[i+1]==(0,0))
    )
    rewards.append(r)
#generate training data 
generator=TrainingDataGenerator(target_x=0,target_y=0)
X,y=generator.generate(path)
bee.brain.train(X,y,rewards,epochs=20)
