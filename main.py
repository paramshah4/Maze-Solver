#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 19:09:48 2021

@author: paramshah
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 10:15:34 2021

@author: paramshah
"""

import random
from SortedSetAstar import *
from GridGenerator import *
from Utility import *
import pandas as pd
import matplotlib.pyplot as plt
from os.path import exists





n = 101
startX = 0
startY = 0

total_solvable=0
solvability=[]

heuristics=["Manhattan","Eucledian","Chernobyl"]
prob=[0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.60]
#prob=[0.25,0.26,0.27,0.28,0.29,0.30,0.31,0.32,0.33,0.34,0.35]

for p in prob:
    print("START")
    total_solvable=0
    for i in range(1000):
        Matrix = Utility.matrixGenerator(n,p)
        path_len,trajectory_length,time_seconds,nodes_exp,found_path=AStarSearch(Matrix, startX, startY ,n-1,n-1,n,p,"Manhattan").solve1()
        if(found_path is True):
            total_solvable=total_solvable+1
    solvability.append(total_solvable)
    
plt.plot(prob, solvability)
plt.xlabel("Density")
plt.ylabel("Solvability")
plt.title("Density Vs Solvability")
plt.show()







