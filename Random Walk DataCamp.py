# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 12:59:58 2022

@author: jdbur
"""

#Random Walk Simulation

#Load Packages
import numpy as np #Numpy
import matplotlib.pyplot as plt

#Set Seed
np.random.seed(123)

#Define Dice function
def dice():
    """Generates Random Number Between 1 and 6 """
    dice_roll = np.random.randint(1, 7)
    return dice_roll

#Initialize Random Walk Distribution
random_walk_dist = []

#Random Walk Distribution
for walk in range(100):
    #Initialize Random Walk
    random_walk = [0]

    #Random Walk Loop
    for step in range(100):
        step = random_walk[-1] #Sets the last value of random_walk as
                               #the current Step
        #Simulate Dice
        dice1 = dice()
        dice2 = dice()
        clumsiness = np.random.rand() #Simulates Mistakes
        
        if dice1 <= 2:
            step = max(0, step - 1) #Sets Lowest Possible Value to 0
                                    #Rolling a 1 or 2 takes 1 Step away
        elif dice1 <= 5:
            step += 1 #Rolling a 3, 4, or 5 adds 1 Step
        else:
            step += dice2 #Rolling a 6 rolls another dice 
                         #The dice's value is added to steps
        
        #Implement Clumsiness
        if clumsiness <= 0.001:
            step = 0 #Making a Mistake Resets to 0
        
        #Append Steps to Random Walk
        random_walk.append(step)
        
    #Append Walks to Random Walk Distribution
    random_walk_dist.append(random_walk)

#Convert to Array
np_random_walk_dist = np.array(random_walk_dist)

#Transpose
np_random_walk_dist_t = np.transpose(np_random_walk_dist)
    
print(np_random_walk_dist_t)

#Plot Random Walk Distribution
plt.plot(np_random_walk_dist_t)
plt.show()

#Chances of Reaching 69th Floor
ends = np_random_walk_dist_t[-1, :]
floor_69 = np.count_nonzero(ends >= 69)

#Plot All Random Walk Simulations
plt.hist(ends)
plt.show()