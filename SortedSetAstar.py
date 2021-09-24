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
class AStarSearch:
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
        self.pathCount = 0
        self.nodeExplored = 0
        self.isMazeSolved = False
        self.probability = probability
        self.queue = SortedSet()
        self.parent={}
        self.discovered_grid=[[1 for x in range(n)] for y in range(n)]
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

    def aStar(self,x,y):
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
        #self.pathCount = 0
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
                
                x_temp = AStarSearch.x_cord[i] + curr_x
                y_temp = AStarSearch.y_cord[i] + curr_y

                if (x_temp >=0 and x_temp < self.size and y_temp >=0 and y_temp <self.size
                    and visited[x_temp][y_temp] == 0 and self.matrix[x_temp][y_temp]==1):
                    
                    
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
        self.isMazeSolved = self.aStar(self.x, self.y)
        return self.isMazeSolved
       
        
       
    def pqReplace(self,x_cord,y_cord,parent_x,parent_y):
        temp_queue = PriorityQueue()
        while(self.queue.empty() is False):
            currcord=self.queue.get()
            if(currcord.x==x_cord and currcord.y==y_cord):
                currcord.h=self.distanceFromGoal(x_cord,y_cord)
                currcord.g=self.distanceFromSource(parent_x,parent_y,x_cord,y_cord)
                currcord.priority=currcord.g+currcord.h
                
            temp_queue.put(currcord)
        return temp_queue
                
    
    def getPathlength(self):
        currnode=(self.goal_x,self.goal_y)
        findpath=[]
        findpath.append(currnode)
        #res=True
        # print(currnode)
        # print(self.x,self.y)
        self.pathCount = 0
        while(currnode != (self.x,self.y)):
            # print("---start----")
            # print(currnode)
            # print("----end---")
            self.pathCount += 1
            findpath.append(self.parent[currnode])
            currnode=self.parent[currnode]
        
        
        
    def findPath(self):
        currnode=(self.goal_x,self.goal_y)
        findpath=[]
        findpath.append(currnode)
        res=True
        # print(currnode)
        # print(self.x,self.y)
        self.pathCount = 0
        while(currnode != (self.x,self.y)):
            # print("---start----")
            # print(currnode)
            # print("----end---")
            findpath.append(self.parent[currnode])
            currnode=self.parent[currnode]
        
        # print("Path is:")
        # print(findpath[::-1])
        findpathrev=findpath[::-1]
        self.pathCount = len(findpath)
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
                self.trajectory_length=self.trajectory_length+1
                self.discovered_grid[coordx][coordy]=self.matrix[coordx][coordy]
                for i in range(0,4):
                    x_temp = AStarSearch.x_cord[i] + coordx
                    y_temp = AStarSearch.y_cord[i] + coordy
                    if (x_temp >=0 and x_temp < self.size and y_temp >=0 and y_temp <self.size):
                        self.discovered_grid[x_temp][y_temp]=self.matrix[x_temp][y_temp]
        if(flag is True):
            res=self.aStar(self.parent[(blockx,blocky)][0],self.parent[(blockx,blocky)][1])
            if(res is True):
                 return self.findPath()
        return res
        
        
        
        
        
    def solve1(self):
        old_time = datetime.datetime.now()
        finalSolvable= self.aStarUtil()
        new_time = datetime.datetime.now()
        time_in_seconds=(new_time - old_time).total_seconds()
        #print((new_time - old_time).total_seconds())
        # print("Node Explored:")
        # print(self.nodeExplored)
        if(finalSolvable is False):
            self.trajectory_length=0
            self.pathCount=1
            self.nodeExplored=0
            
        return self.pathCount,self.trajectory_length,time_in_seconds,self.nodeExplored,finalSolvable

    
    
    
    
    

    
    
    
    
    

