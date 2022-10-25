from functools import reduce
from math import sqrt
import numpy as np

np.set_printoptions(formatter={'float' : lambda x: "{0:0.3f}".format(x)})
def translate(Tx, Ty, Tz):
    return [[1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [Tx,Ty,Tz,1]]

def eyeCS(x,y,z, D, S):
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
    product = reduce(np.dot, [translate(x,y,z), static_matrix, y_rotation, x_rotation, z_rotation, view_distance])

    return product

#eyeCS(6,8,7.5,60, 15)