import draw3D as shape
import transformations as trans
import prompt

ans = int(input("Please enter a shape you want to draw\n1)Cube\n2)Triangular Prism\n"))

if ans == 1:
    shape.draw_cube()
    prompt.prompt_transformation("cube")
elif ans == 2:
    shape.draw_triangular_prism()
else: 
    print("Invalid answer! Please try again.")