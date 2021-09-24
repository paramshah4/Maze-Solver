# this is a grid generator class that produces the maze based
# on the matrix passed to it.
from graphics import *
class GridGenerator:
    def __init__(self,matrix,type):
        self.matrix =  matrix
        self.type = type
    def generate_grid(self,n , size, windowsize):
        win = GraphWin(self.type, windowsize, windowsize)
        matrix = self.matrix
        for i in range(0, n, 1):
            for j in range(0, n, 1):
                rect = Rectangle(Point(j*size, i*size), Point((j+1)*size, (i+1)*size))
                rect.setWidth(3)
                if matrix[i][j] ==0:  # Keeps the block empty if probability is lesser than 0.2
                    rect.setFill("Black")
                else:
                    rect.setFill("White")
                if (i == 0 and j == 0):
                    rect.setFill("Green")
                if (i == n-1 and j == n-1):
                    rect.setFill("Red")
                rect.draw(win)
        return win
