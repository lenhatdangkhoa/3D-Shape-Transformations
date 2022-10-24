from PIL import Image
import math
import numpy as np
import transformations as trans
# Creating a 250 x 250 plain black image
image = Image.new(mode="RGB", size = (501, 501), color = (0,0,0))

"""
Takes two coordinates and draw a line using the basic line drawing algorithm
"""
def draw_basic_line(x0, y0, x1, y1):

    # If x0 == x1, in other words, it's a vertical line, just draw a vertical line |y1 - y0| times.
    if x0 == x1:
        smaller_y_value = min(y0,y1)
        # The critical loop
        for i in range(abs(y1 - y0) + 1):
            if (x0 > -1 and x0 < 501) and (smaller_y_value + i > -1 and smaller_y_value + i < 501):
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
                if (x > -1  and x < 501) and (y > -1 and y < 501):
                    image.putpixel((x,y), (255,255,255))
        # If Δx < Δy, or |x1-x0| < |y1-y0|, draw vertically |y1-y0| times.
        elif (abs(x1-x0)) < (abs(y1-y0)):
            smaller_y_value = min(y0,y1)
            # The critical loop
            for i in range(abs(y1-y0) + 1):
               y = smaller_y_value + i
               x = (y - y_intercept)/slope
               x = math.trunc(x)
               if (x > -1  and x < 501) and (y > -1 and y < 501):
                image.putpixel((x,y), (255,255,255))

coordinates = {
    0: [1,1,1,1],
    1: [2,1,1,1],
    2: [2,2,1,1],
    3: [1,2,1,1],
    4: [1,1,2,1],
    5: [2,1,2,1],
    6: [2,2,2,1],
    7: [1,2,2,1]
}
vertex_table = {
    0: [0,0],
    1: [0,0],
    2: [0,0],
    3: [0,0],
    4: [0,0],
    5: [0,0],
    6: [0,0],
    7: [0,0],
}

for i in coordinates:
    matrix = np.dot(coordinates[i], trans.translate(0,0,0))
    coordinates[i] = matrix
    #print(f"{matrix[0]} {matrix[1]} {matrix[2]} {matrix[3]}")

for i in coordinates:
    x = ((7.5 * coordinates[i][0]) / (15 * coordinates[i][2])) * 250 + 250
    y = ((7.5 * coordinates[i][1]) / (15 * coordinates[i][2])) * 250 + 250
    vertex_table[i] = [math.trunc(x), math.trunc(y)]





draw_basic_line(
    vertex_table[0][0], vertex_table[0][1],
    vertex_table[1][0], vertex_table[1][1]
)
draw_basic_line(
    vertex_table[1][0], vertex_table[1][1],
    vertex_table[2][0], vertex_table[2][1]
)
draw_basic_line(
    vertex_table[2][0], vertex_table[2][1],
    vertex_table[3][0], vertex_table[3][1]
)
draw_basic_line(
    vertex_table[3][0], vertex_table[3][1],
    vertex_table[0][0], vertex_table[0][1]
)

draw_basic_line(
    vertex_table[4][0], vertex_table[4][1],
    vertex_table[5][0], vertex_table[5][1]
)
draw_basic_line(
    vertex_table[5][0], vertex_table[5][1],
    vertex_table[6][0], vertex_table[6][1]
)
draw_basic_line(
    vertex_table[6][0], vertex_table[6][1],
    vertex_table[7][0], vertex_table[7][1]
)
draw_basic_line(
    vertex_table[7][0], vertex_table[7][1],
    vertex_table[4][0], vertex_table[4][1]
)

draw_basic_line(
    vertex_table[0][0], vertex_table[0][1],
    vertex_table[4][0], vertex_table[4][1]
)
draw_basic_line(
    vertex_table[1][0], vertex_table[1][1],
    vertex_table[5][0], vertex_table[5][1]
)
draw_basic_line(
    vertex_table[2][0], vertex_table[2][1],
    vertex_table[6][0], vertex_table[6][1]
)
draw_basic_line(
    vertex_table[3][0], vertex_table[3][1],
    vertex_table[7][0], vertex_table[7][1]
)

image.show()