from PIL import Image
import math

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

draw_basic_line(375, 375, 500, 375)
draw_basic_line(500, 375, 500, 500)
draw_basic_line(500, 500, 375, 500)
draw_basic_line(375, 500, 375, 375)

draw_basic_line(313,313,375,313)
draw_basic_line(375,313, 375, 375)
draw_basic_line(375,375, 313, 375)
draw_basic_line(313,375,313,313)

draw_basic_line(375,375,313,313)
draw_basic_line(500,375,375,313)
draw_basic_line(500,500,375,375)
draw_basic_line(375,500,313,375)
"""


draw_basic_line(375,375,375,125)
draw_basic_line(375,125,125,125)
"""
image.show()