from PIL import Image
import math
import numpy as np
import transformations as trans
import csv
from decimal import Decimal
import decimal

# Creating a 1024 plain black image
image = Image.new(mode="RGB", size = (1024, 1024), color = (0,0,0))

np.set_printoptions(formatter={'float' : lambda x: "{0:0.3f}".format(x)}) # Setting the decimal value for matrix combinations to be 3 decimal places

decimal.getcontext().prec = 3 # Used for floats, up to 3 decimal places

"""
Takes two coordinates and draw a line using the basic line drawing algorithm
"""
def draw_basic_line(x0, y0, x1, y1):

    # If x0 == x1, in other words, it's a vertical line, just draw a vertical line |y1 - y0| times.
    if x0 == x1:
        smaller_y_value = min(y0,y1)
        # The critical loop
        for i in range(abs(y1 - y0) + 1):
            if (x0 > -1 and x0 < 1024) and (smaller_y_value + i > -1 and smaller_y_value + i < 1024):
                image.putpixel((x0, smaller_y_value + i), (255,255,255))

    # Else, find the equation of the line using two points and draw a line accordingly
    else:
        
        slope = (y1 - y0) / (x1 - x0)
        y_intercept = y1 - (slope * x1)

        # If Δx >= Δy, or |x1-x0| >= |y1-y0|, draw horizontally |x1-x0| times.
        if (abs(x1 - x0)) >= (abs(y1-y0)):

            smaller_x_value = min(x0, x1)
            # The critical loop
            for i in range(abs(x1 - x0) + 1):
                x = smaller_x_value + i
                y = (slope * x) + y_intercept
                y = math.trunc(y)
                if (x > -1  and x < 1024) and (y > -1 and y < 1024):
                    image.putpixel((x,y), (255,255,255))
        # If Δx < Δy, or |x1-x0| < |y1-y0|, draw vertically |y1-y0| times.
        elif (abs(x1-x0)) < (abs(y1-y0)):
            smaller_y_value = min(y0,y1)
            # The critical loop
            for i in range(abs(y1-y0) + 1):
               y = smaller_y_value + i
               x = (y - y_intercept)/slope
               x = math.trunc(x)
               if (x > -1  and x < 1024) and (y > -1 and y < 1024):
                image.putpixel((x,y), (255,255,255))

# Transform from World Coordinate System to Eye Coordinate System. 
eye_transformation = trans.eyeCS(6,8,7.5,60,15)

# Draw the cube and displaying it
cube_coordinates = {}

# Read coordinates from "cube_coordinates.csv" and assign them to the dictionary coordinates
with open("cube_coordinates.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    i = 0
    for line in csvreader:
        temp = []
        for num in line:
            temp.append(int(num))
        cube_coordinates[int(i)] = temp
        i += 1
        
# Transform all points in cube coordinates to ECS
for i in cube_coordinates:
    matrix = np.dot(cube_coordinates[i], eye_transformation)
    cube_coordinates[i] = matrix

# Converting (x,y,z) to (x', y') using perspective projection
cube_vertex_table = {}
for i in cube_coordinates:
    x = (cube_coordinates[i][0] / cube_coordinates[i][2]) * 511.5 + 511.5
    y = (cube_coordinates[i][1] / cube_coordinates[i][2]) * 511.5 + 511.5
    cube_vertex_table[i] = [math.trunc(x), math.trunc(y)]

# Display the cube
def draw_cube():
    draw_basic_line(
        cube_vertex_table[0][0], cube_vertex_table[0][1],
        cube_vertex_table[1][0], cube_vertex_table[1][1]
    )
    draw_basic_line(
        cube_vertex_table[1][0], cube_vertex_table[1][1],
        cube_vertex_table[2][0], cube_vertex_table[2][1]
    )
    draw_basic_line(
        cube_vertex_table[2][0], cube_vertex_table[2][1],
        cube_vertex_table[3][0], cube_vertex_table[3][1]
    )
    draw_basic_line(
        cube_vertex_table[3][0], cube_vertex_table[3][1],
        cube_vertex_table[0][0], cube_vertex_table[0][1]
    )

    draw_basic_line(
        cube_vertex_table[4][0], cube_vertex_table[4][1],
        cube_vertex_table[5][0], cube_vertex_table[5][1]
    )
    draw_basic_line(
        cube_vertex_table[5][0], cube_vertex_table[5][1],
        cube_vertex_table[6][0], cube_vertex_table[6][1]
    )
    draw_basic_line(
        cube_vertex_table[6][0], cube_vertex_table[6][1],
        cube_vertex_table[7][0], cube_vertex_table[7][1]
    )
    draw_basic_line(
        cube_vertex_table[7][0], cube_vertex_table[7][1],
        cube_vertex_table[4][0], cube_vertex_table[4][1]
    )

    draw_basic_line(
        cube_vertex_table[0][0], cube_vertex_table[0][1],
        cube_vertex_table[4][0], cube_vertex_table[4][1]
    )
    draw_basic_line(
        cube_vertex_table[1][0], cube_vertex_table[1][1],
        cube_vertex_table[5][0], cube_vertex_table[5][1]
    )
    draw_basic_line(
        cube_vertex_table[2][0], cube_vertex_table[2][1],
        cube_vertex_table[6][0], cube_vertex_table[6][1]
    )
    draw_basic_line(
        cube_vertex_table[3][0], cube_vertex_table[3][1],
        cube_vertex_table[7][0], cube_vertex_table[7][1]
    )
    image.show()

triangle_coordinates = {}
# Read coordinates from "triangular_prism_coordinates.csv" and assign them to the dictionary triangle coordinates
with open("triangular_prism_coordinates.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    i = 0
    for line in csvreader:
        temp = []
        for num in line:
            temp.append(int(num))
        triangle_coordinates[int(i)] = temp
        i += 1

# Transform all points in triangle coordinates to ECS
for i in triangle_coordinates:
    matrix = np.dot(triangle_coordinates[i], eye_transformation)
    triangle_coordinates[i] = matrix

# Converting (x,y,z) to (x', y') using perspective projection
triangle_vertex_table = {}
for i in triangle_coordinates:
    x = Decimal((triangle_coordinates[i][0] / triangle_coordinates[i][2]) * 511.5 + 511.5)
    y = Decimal((triangle_coordinates[i][1] / triangle_coordinates[i][2]) * 511.5 + 511.5)
    triangle_vertex_table[i] = [(math.trunc(x)), math.trunc(y)]

# Display the triangular prism
def draw_triangular_prism():   
    draw_basic_line(
        triangle_vertex_table[0][0], triangle_vertex_table[0][1],
        triangle_vertex_table[1][0], triangle_vertex_table[1][1]
    )
    draw_basic_line(
        triangle_vertex_table[1][0], triangle_vertex_table[1][1],
        triangle_vertex_table[2][0], triangle_vertex_table[2][1]
    )
    draw_basic_line(
        triangle_vertex_table[2][0], triangle_vertex_table[2][1],
        triangle_vertex_table[3][0], triangle_vertex_table[3][1]
    )
    draw_basic_line(
        triangle_vertex_table[3][0], triangle_vertex_table[3][1],
        triangle_vertex_table[0][0], triangle_vertex_table[0][1]
    )
    draw_basic_line(
        triangle_vertex_table[0][0], triangle_vertex_table[0][1],
        triangle_vertex_table[4][0], triangle_vertex_table[4][1]
    )
    draw_basic_line(
        triangle_vertex_table[1][0], triangle_vertex_table[1][1],
        triangle_vertex_table[5][0], triangle_vertex_table[5][1]
    )
    draw_basic_line(
        triangle_vertex_table[4][0], triangle_vertex_table[4][1],
        triangle_vertex_table[5][0], triangle_vertex_table[5][1]
    )
    draw_basic_line(
        triangle_vertex_table[2][0], triangle_vertex_table[2][1],
        triangle_vertex_table[5][0], triangle_vertex_table[5][1]
    )
    draw_basic_line(
        triangle_vertex_table[3][0], triangle_vertex_table[3][1],
        triangle_vertex_table[4][0], triangle_vertex_table[4][1]
    )
    image.show()

"""
Resetting the image back to the original 1024x1024 black image.
"""
def clear_image():
    for y in range(1024):
        for x in range(1024):
            image.putpixel((x,y), (0,0,0))


