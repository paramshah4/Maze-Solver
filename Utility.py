import random
import numpy as np
from DFS import *
from BFS import *
from AStar import *
#Helper class for simulated Annealing and Genetic Algorithm and Matrix Generator
class Utility:
   @staticmethod
   def shuffle(matrix):
       n  = len(matrix)
       matrix = np.ravel(matrix,1)
       np.random.shuffle(matrix)
       matrix = matrix.reshape(n,n)
       matrix[0][0]=1
       matrix[n-1][n-1]=1
       return matrix

   @staticmethod
   def performMutation(self):
       print("gautam")

   @staticmethod
   def performCrossOver(self):
       print("yes")

   @staticmethod
   def matrixGenerator(n,p):
        Matrix = [[0 for x in range(n)] for y in range(n)]
        for i in range(0, n, 1):
            for j in range(0, n, 1):
                prob = random.random()
                if prob > p:
                    Matrix[i][j] = 1
        Matrix[n-1][n-1] = 1
        Matrix[0][0]=1
        return Matrix

   @staticmethod
   def getAlgo(type,Matrix,startX,startY,n,grid,size,p):
       if type=="DFS":
           return DFS(Matrix, startX, startY, n - 1, n - 1, grid, n, size,p,False)
       if type=="BFS":
           return BFS(Matrix,startX,startY,n-1,n-1,grid,n,size,p,False)
       if type == "AStar":
           return AStar(Matrix,startX,startY,n-1,n-1,grid,n,size,p,"Manhatten",False)
       if type == "AStar Euclidean":
           return AStar(Matrix,startX,startY,n-1,n-1,grid,n,size,p,"Euclidean",False)