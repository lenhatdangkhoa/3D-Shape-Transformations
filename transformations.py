from functools import reduce
import math
from math import sqrt
import numpy as np

np.set_printoptions(formatter={'float' : lambda x: "{0:0.3f}".format(x)}) # Setting the decimal value for matrix combinations to be 3 decimal places

# Return a 4x4 translation matrix
def translate(Tx, Ty, Tz):
    return [[1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [Tx,Ty,Tz,1]]

# Return a 4x4 scaling matrix at the center of scale (Cx, Cy, Cz)
def scale(x,y,z, Cx, Cy, Cz):
    move = translate(-Cx,-Cy,-Cz)
    scales = [[x,0,0,0],
            [0,y,0,0],
            [0,0,z,0],
            [0,0,0,1]]
    move2 = translate(Cx,Cy,Cz)
    return reduce(np.dot, [move, scales, move2])

# Return a 4x4 rotation matrix around the z-axis
def z_rotate(angle):
    return [[math.cos(math.radians(angle)), math.sin(math.radians(angle)), 0, 0],
            [-math.sin(math.radians(angle)), math.cos(math.radians(angle)), 0, 0],
            [0,0,1,0],
            [0,0,0,1]]

# Return a 4x4 rotation matrix around the y-axis
def y_rotate(angle):
    return [[math.cos(math.radians(angle)),0, -math.sin(math.radians(angle)), 0],
            [0,1,0,0],
            [math.sin(math.radians(angle)),0,math.cos(math.radians(angle)),0],
            [0,0,0,1]]

# Return a 4x4 rotation matrix around the x-axis
def x_rotate(angle):
    return [[1,0,0,0],
            [0, math.cos(math.radians(angle)), math.sin(math.radians(angle)),0],
            [0, -math.sin(math.radians(angle)), math.cos(math.radians(angle)),0],
            [0,0,0,1]]

"""
Return a 4x4 eye coordinate system transformation matrix. D is the distance from the screen for optimal view half of the screen's size.
x,y,z are coordinates of the eye.
"""
def eyeCS(x,y,z, D, S):
    trans_matrix = translate(-x,-y,-z)
    static_matrix =  [[1,0,0,0],
                     [0,0,-1,0],
                     [0,1,0,0],
                     [0,0,0,1]]
    y_rotation = [[-(y/(sqrt(x**2 + y**2))), 0, x/(sqrt(x**2 + y**2)), 0],
                  [0,1,0,0],
                  [-(x/(sqrt(x**2 + y**2))), 0 , -(y/(sqrt(x**2 + y**2))), 0],
                  [0,0,0,1]]
    x_rotation = [[1,0,0,0],
                  [0,(sqrt(x**2 + y**2))/sqrt(z**2 + (sqrt(x**2 + y**2))**2), z/sqrt(z**2 + (sqrt(x**2 + y**2))**2), 0],
                  [0, -(z/sqrt(z**2 + (sqrt(x**2 + y**2))**2)), (sqrt(x**2 + y**2))/sqrt(z**2 + (sqrt(x**2 + y**2))**2), 0],
                  [0,0,0,1]]
    z_rotation = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,-1,0],
                  [0,0,0,1]]
    view_distance = [[D/S,0,0,0],
                     [0,D/S,0,0],
                     [0,0,1,0],
                     [0,0,0,1]]
    product = reduce(np.dot, [trans_matrix, static_matrix, y_rotation, x_rotation, z_rotation, view_distance])
    return product

