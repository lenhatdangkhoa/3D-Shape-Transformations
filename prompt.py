import draw3D
import transformations as trans
import math
import numpy as np
from decimal import Decimal
import decimal

decimal.getcontext().prec = 3 # Used for floats, up to 3 decimal places

"""
Prompting the user for transformations they wish to apply to the shape
"""
def prompt_transformation(shape):
    ans = 0
    while ans != 4:
        ans = int(input("Transformation:\n1)Translate\n2)Scale\n3)Rotate\n4)Quit\n"))
        if shape == "cube":
            if ans == 1:
                Tx = float(input("Enter x displacement: "))
                Ty = float(input("Enter y displacement: "))
                Tz = float(input("Enter z displacement: "))
                redraw_cube(trans.translate(Tx,Ty,Tz))
            elif ans == 2:
                x = float(input("Enter x scaling factor: "))
                y = float(input("Enter y scaling factor: "))
                z = float(input("Enter z scaling factor: "))
                Cx = float(input("Enter x-center: "))
                Cy = float(input("Enter y-center: "))
                Cz = float(input("Enter z-center: "))
                redraw_cube(trans.scale(x,y,z,Cx,Cy,Cz))
            elif ans == 3:
                angle = float(input("Enter the angle of rotation: "))
                rotation_axis = int(input("Which axis do you want to rotate around?\n1)x\n2)y\n3)z\n"))
                if rotation_axis == 1:
                    redraw_cube(trans.x_rotate(angle))
                elif rotation_axis == 2:
                    redraw_cube(trans.y_rotate(angle))
                elif rotation_axis == 3:
                    redraw_cube(trans.z_rotate(angle))
                else:
                    print("Invalid input! Please try again.")

        else:
            if ans == 1:
                Tx = float(input("Enter x displacement: "))
                Ty = float(input("Enter y displacement: "))
                Tz = float(input("Enter z displacement: "))
                redraw_triangle(trans.translate(Tx,Ty,Tz))
            elif ans == 2:
                x = float(input("Enter x scaling factor: "))
                y = float(input("Enter y scaling factor: "))
                z = float(input("Enter z scaling factor: "))
                Cx = float(input("Enter x-center: "))
                Cy = float(input("Enter y-center: "))
                Cz = float(input("Enter z-center: "))
                redraw_triangle(trans.scale(x,y,z,Cx,Cy,Cz))
            elif ans == 3:
                angle = float(input("Enter the angle of rotation: "))
                rotation_axis = int(input("Which axis do you want to rotate around?\n1)x\n2)y\n3)z\n"))
                if rotation_axis == 1:
                    redraw_triangle(trans.x_rotate(angle))
                elif rotation_axis == 2:
                    redraw_triangle(trans.y_rotate(angle))
                elif rotation_axis == 3:
                    redraw_triangle(trans.z_rotate(angle))
                else:
                    print("Invalid input! Please try again.")


"""
Redrawing the cube by applying the transformation matrix to each points in the cube coordinates.
"""
def redraw_cube(transformation_matrix):
    draw3D.clear_image() # Reset the image back to the original 1024x1024 black image

    # Apply transformations to each point in cube coordinates
    for i in draw3D.cube_coordinates:
        matrix = np.dot(draw3D.cube_coordinates[i], transformation_matrix)
        draw3D.cube_coordinates[i] = matrix

    # Converting (x,y,z) to (x', y') using perspective projection
    draw3D.cube_vertex_table = {}
    for i in draw3D.cube_coordinates:
        x = Decimal((draw3D.cube_coordinates[i][0] / draw3D.cube_coordinates[i][2]) * 511.5 + 511.5)
        y = Decimal((draw3D.cube_coordinates[i][1] / draw3D.cube_coordinates[i][2]) * 511.5 + 511.5)
        draw3D.cube_vertex_table[i] = [math.trunc(x), math.trunc(y)]

    draw3D.draw_cube()

"""
Redrawing the triangular prism by applying the transformation matrix to each points in the triagle coordinates.
"""
def redraw_triangle(transformation_matrix):
    draw3D.clear_image() # Reset the image back to the original 1024x1024 black image

    # Apply transformations to each point in triangle coordinates
    for i in draw3D.triangle_coordinates:
        matrix = np.dot(draw3D.triangle_coordinates[i], transformation_matrix)
        draw3D.triangle_coordinates[i] = matrix

    # Converting (x,y,z) to (x', y') using perspective projection
    draw3D.cube_vertex_table = {}
    for i in draw3D.triangle_coordinates:
        x = Decimal((draw3D.triangle_coordinates[i][0] / draw3D.triangle_coordinates[i][2]) * 511.5 + 511.5)
        y = Decimal((draw3D.triangle_coordinates[i][1] / draw3D.triangle_coordinates[i][2]) * 511.5 + 511.5)
        draw3D.triangle_vertex_table[i] = [math.trunc(x), math.trunc(y)]

    draw3D.draw_triangular_prism()