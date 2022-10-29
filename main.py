import draw3D as shape
import prompt

"""
This is the main method where the user can display shapes and apply transformations to them.
"""
def start_program():
    ans = int(input("Please enter a shape you want to draw\n1)Cube\n2)Triangular Prism\n"))
    if ans == 1:
        shape.draw_cube()
        prompt.prompt_transformation("cube")
    elif ans == 2:
        shape.draw_triangular_prism()
        prompt.prompt_transformation("triangular_prism")
    else: 
        print("Invalid answer! Please try again.")
        
if __name__ == "__main__":
    start_program()