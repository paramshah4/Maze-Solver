#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 20:04:41 2021

@author: paramshah
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:50:22 2021

@author: paramshah
"""
from sortedcontainers import SortedSet
from queue import PriorityQueue
import math
import datetime


#Coordinates(f,h,g,x,y)
#Coordinates(0,1,2,3,4)
class RepeatedAStarSearch:
    x_cord = [0, 1, 0, -1]
    y_cord = [1, 0, -1, 0]
    childs=[]


    def __init__(self,matrix, startX, startY,goalX,goalY,n,probability,type):
        self.x = startX
        self.y = startY
        self.goal_x = goalX
        self.goal_y = goalY
        self.matrix = matrix
        self.size = n
        self.type = type
        self.map = {}
        self.nodeExplored = 0
        self.isMazeSolved = False
        self.probability = probability
        self.queue = SortedSet()
        self.parent={}
        self.discovered_grid=[[1 for x in range(n)] for y in range(n)]
        self.traverse_discovered_grid=[[0 for x in range(n)] for y in range(n)]
        self.trajectory_length=0
        self.dict_poppedpq={}



    def distanceFromGoal(self,x1, y1):
         if self.type == "Manhattan":
            return abs(self.goal_x - x1) + abs(self.goal_y-y1)
         elif self.type=="Eucledian":
             return  math.sqrt((self.goal_x - x1)**2 + (self.goal_y - y1)**2)
         else:
             return max(abs(self.goal_x - x1), abs(self.goal_y-y1))

    def distanceFromSource(self,x_parent, y_parent,x_current,y_current):
        if self.map.get(tuple([x_current,y_current])) == None:
            self.map[tuple([x_current,y_current])] = self.map.get(tuple([x_parent,y_parent]))+1
            self.parent[(x_current,y_current)]=(x_parent,y_parent)
        else:
            if(self.map.get(tuple([x_parent,y_parent]))+1 < self.map.get(tuple([x_current,y_current]))):
                self.map[tuple([x_current,y_current])]=self.map.get(tuple([x_current,y_current]))
            else:
                self.map[tuple([x_current,y_current])]=self.map.get(tuple([x_parent,y_parent]))+1
                self.parent[(x_current,y_current)]=(x_parent,y_parent)

        return self.map.get(tuple([x_current,y_current]))

    def aStar(self,x,y,matrix):
        # print("ASTARR--------------------")
        #self.map[tuple([x,y])] = 0
        visited = [[0 for x in range(self.size)] for y in range(self.size)]
        self.map = {}
        self.dict_poppedpq={}
        self.parent={}
        self.queue.clear()
        self.map[tuple([x,y])] = 0
        self.queue.add((self.distanceFromGoal(x,y),self.distanceFromGoal(x,y),0,x,y))
        self.x=x
        self.y=y
        while self.queue.__len__() > 0:
            #print(self.queue)
            curr_fn,curr_hn,curr_gn,curr_x,curr_y = self.queue.pop(0)

            if(curr_x==self.goal_x and curr_y==self.goal_y):
                return True

            if visited[curr_x][curr_y] ==1:
               continue
           
            self.nodeExplored += 1

            visited[curr_x][curr_y] = 1

            for i in range(0,4):
                
                x_temp = RepeatedAStarSearch.x_cord[i] + curr_x
                y_temp = RepeatedAStarSearch.y_cord[i] + curr_y

                if (x_temp >=0 and x_temp < self.size and y_temp >=0 and y_temp <self.size
                    and visited[x_temp][y_temp] == 0 and matrix[x_temp][y_temp]==1):
                    
                    
                    hn=self.distanceFromGoal(x_temp,y_temp)
                    gn=self.distanceFromSource(curr_x,curr_y,x_temp,y_temp)
                    fn=gn+hn
                    
                    if (x_temp,y_temp) in self.dict_poppedpq:
                        fnold,hnold,gnold=self.dict_poppedpq[(x_temp,y_temp)]
                        self.queue.remove((fnold,hnold,gnold,x_temp,y_temp))
                        

                    self.dict_poppedpq[(x_temp,y_temp)]=(fn,hn,gn)

                    self.queue.add((fn,hn,gn,x_temp,y_temp))
        return False

    def aStarUtil(self):
        self.isMazeSolved = self.aStar(self.x, self.y,self.discovered_grid)
        if(self.isMazeSolved is True):
            
            return self.findPath()
                
        
        return self.isMazeSolved
       
        
      
                
    
    def getPathlength(self):
        currnode=(self.goal_x,self.goal_y)
        findpath=[]
        findpath.append(currnode)
        #res=True
        # print(currnode)
        # print(self.x,self.y)
        pathCount=0
        while(currnode != (self.x,self.y)):
            # print("---start----")
            # print(currnode)
            # print("----end---")
            pathCount += 1
            findpath.append(self.parent[currnode])
            currnode=self.parent[currnode]
            
        return pathCount
        
        
        
    def findPath(self):
        currnode=(self.goal_x,self.goal_y)
        findpath=[]
        findpath.append(currnode)
        res=True
        trajcount=0
        # print(currnode)
        # print(self.x,self.y)

        while(currnode != (self.x,self.y)):
            # print("---start----")
            # print(currnode)
            # print("----end---")
            findpath.append(self.parent[currnode])
            currnode=self.parent[currnode]
        
        # print("Path is:")
        # print(findpath[::-1])
        findpathrev=findpath[::-1]
        flag=False
        blockx=0
        blocky=0
        for tuplecoord in findpathrev:
            
            coordx=tuplecoord[0]
            coordy=tuplecoord[1]
            if self.matrix[coordx][coordy]==0:
                self.discovered_grid[coordx][coordy]=self.matrix[coordx][coordy]
                flag=True
                blockx=coordx
                blocky=coordy
                break
            else:
                #self.trajectory_length=self.trajectory_length+1
                trajcount=trajcount+1
                self.discovered_grid[coordx][coordy]=self.matrix[coordx][coordy]
                self.traverse_discovered_grid[coordx][coordy]=self.matrix[coordx][coordy]
                for i in range(0,4):
                    x_temp = RepeatedAStarSearch.x_cord[i] + coordx
                    y_temp = RepeatedAStarSearch.y_cord[i] + coordy
                    if (x_temp >=0 and x_temp < self.size and y_temp >=0 and y_temp <self.size):
                        self.discovered_grid[x_temp][y_temp]=self.matrix[x_temp][y_temp]
                        self.traverse_discovered_grid[x_temp][y_temp]=self.matrix[x_temp][y_temp]
                        
        self.trajectory_length=self.trajectory_length+trajcount-1
        if(flag is True):
            #print(self.parent[(blockx,blocky)][0],self.parent[(blockx,blocky)][1])
            res=self.aStar(self.parent[(blockx,blocky)][0],self.parent[(blockx,blocky)][1],self.discovered_grid)
            if(res is True):
                 return self.findPath()
        return res
        
        
        
        
        
    def solve1(self):
        old_time = datetime.datetime.now()
        finalSolvable= self.aStarUtil()
        new_time = datetime.datetime.now()
        time_in_seconds=(new_time - old_time).total_seconds()
        
        nodesexp=self.nodeExplored
        

        
        
        if(finalSolvable is True):
            self.aStar(0,0,self.traverse_discovered_grid)
            discovered_len=self.getPathlength()
            
            self.aStar(0,0,self.matrix)
            matrix_len=self.getPathlength()
        else:
            self.trajectory_length=0
            self.nodeExplored=0
            matrix_len=0
            discovered_len=0
            
        return matrix_len,discovered_len,self.trajectory_length,time_in_seconds,nodesexp,finalSolvable

    
    
    
    
    

    
    
    
    
    

