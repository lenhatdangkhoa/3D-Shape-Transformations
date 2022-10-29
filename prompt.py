import draw3D
import transformations as trans
import math
import numpy as np

def prompt_transformation(shape):
    ans = 0
    while ans != 4:
        ans = int(input("Transformation:\n1)Translate\n2)Scale\n3)Rotate\n4)Quit\n"))
        if shape == "cube":
            if ans == 1:
                Tx = float(input("Enter x displacement: "))
                Ty = float(input("Enter y displacement: "))
                Tz = float(input("Enter z displacement: "))
                redraw(trans.translate(Tx,Ty,Tz))
            elif ans == 2:
                x, y, z = int(input("Enter x, y, and z scaling factors: "))
                Cx, Cy, Cz = int(input("Enter the center of scale: "))
                redraw(trans.scale(x,y,z,Cx,Cy,Cz))
            elif ans == 3:
                angle = float(input("Enter the angle of rotation: "))
                rotation_axis = int(input("Which axis do you want to rotate around?\n1)x\n2)y\n3)z\n"))
                if rotation_axis == 1:
                    redraw(trans.x_rotate(angle))
                elif rotation_axis == 2:
                    redraw(trans.y_rotate(angle))
                elif rotation_axis == 3:
                    redraw(trans.z_rotate(angle))
                else:
                    print("Invalid input! Please try again.")
        else:
            if ans == 1:
                x, y, z = int(input("Enter x, y, and z displacements: "))
            elif ans == 2:
                x, y, z = int(input("Enter x, y, and z scaling factors: "))
                Cx, Cy, Cz = int(input("Enter the center of scale: "))

def redraw(transformation_matrix):
    # Transform all points in coordinates to ECS
    for i in draw3D.cube_coordinates:
        matrix = np.dot(draw3D.cube_coordinates[i], draw3D.eye_transformation)
        matrix = np.dot(matrix, transformation_matrix)
        draw3D.cube_coordinates[i] = matrix

    #print(draw3D.cube_coordinates)
    # Converting (x,y,z) to (x', y') using perspective projection
    draw3D.cube_vertex_table = {}
    for i in draw3D.cube_coordinates:
        x = (draw3D.cube_coordinates[i][0] / draw3D.cube_coordinates[i][2]) * 511.5 + 511.5
        y = (draw3D.cube_coordinates[i][1] / draw3D.cube_coordinates[i][2]) * 511.5 + 511.5
        draw3D.cube_vertex_table[i] = [math.trunc(x), math.trunc(y)]

    #print(draw3D.cube_vertex_table)
    draw3D.draw_cube(draw3D.cube_vertex_table)

redraw(trans.translate(50,0,0))