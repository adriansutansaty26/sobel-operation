import numpy as np
import cv2 as cv
import math 

matrix = np.array([[1,1,2,3,1,5,6,1],
                   [1,1,5,5,6,7,1,1],
                   [1,1,1,1,6,6,6,6],
                   [1,1,1,2,7,7,7,7],
                   [1,7,7,7,7,6,6,1],
                   [1,7,6,6,6,6,1,1],
                   [0,7,6,6,6,6,1,1],
                   [0,6,6,6,5,1,1,1]])
W = len(matrix[0])
H = len(matrix)
            
new_image = np.zeros((8,8))
txt = np.zeros((3,3))
kernel = np.array([[1, 2, 1],
                   [-1, 1, -1],
                   [1, 2, 1]])
c = 2

for x in range(W-2):
    for y in range(H-2):     
        
        a0 = matrix[x][y]
        a1 = matrix[x][y+1]
        a2 = matrix[x][y+2]
        
        a7 = matrix[x+1][y]
        xy = matrix[x+1][y+1]
        a3 = matrix[x+1][y+2]
        
        a6 = matrix[x+2][y]
        a5 = matrix[x+2][y+1]
        a4 = matrix[x+2][y+2]
        
        
        Gx = (a2+(c*a3)+a4) - (a0+(c*a7)+a6)
        Gy = (a0+(c*a1)+a2) - (a6+(c*a5)+a4)
        Mag = abs(Gx) + abs(Gy) 
        alpha = math.degrees(math.atan(Gy/Gx))
        
        print("-----------------------------------------")
        print("| "+str(a0)+" "+str(a1)+" "+str(a2)+" |   Gradient X = "+str(Gx))
        print("| "+str(a7)+" "+str(xy)+" "+str(a3)+" |   Gradient Y = "+str(Gy))
        print("| "+str(a6)+" "+str(a5)+" "+str(a4)+" |   Magnitude  = "+str(Mag))
        print("            α = "+str(alpha))
