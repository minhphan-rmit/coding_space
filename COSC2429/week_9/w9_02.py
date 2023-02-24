# import
import os

# input
file_name = input('File name: ')
folder_name = input('Folder name: ')

# turtle code
circle_drawing = """import turtle

# canvas setup
win = turtle.Screen()
win.bgcolor("white")

# Initializing the turtle
t = turtle.Turtle()
t.color("black")
t.pensize(5)

def drawing_circle():
    r = 50
    t.circle(r)
win.exitonclick()    
"""

# create file path
file_path = folder_name + '\\' + file_name
# create folder
os.makedirs(folder_name, exist_ok=True)
# open file to write
f = open(file_name, 'w')
# write the code to the file
f.write(circle_drawing)
# close the file
f.close()
