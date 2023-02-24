# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: Individual - Timed Programming Lab Test 1 (25%)
# Author: Phan Nhat Minh (s3978598)
# Created date: 19/11/2022
# Last modified date: 19/11/2022
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11
# Question: 3

import turtle

# canvas setup
win = turtle.Screen()
border = turtle.Turtle()
flag = turtle.Turtle()
star = turtle.Turtle()

# color setup
win.bgcolor("black")
border.color("blue")
star.color("white")
flag.color("red")

# pen size setup
border.pensize(5)


# function to draw the background of the flag
def flag_bg():
    """
    This function is for drawing a red rectangle shape for the flag background
    """
    # move the turtle to the correct position so that the center of the object will be the center of the screen
    flag.penup()
    flag.backward(200)
    flag.left(90)
    flag.forward(100)
    flag.right(90)
    flag.pendown()
    flag.begin_fill()
    # loop for drawing a rectangle
    for i in range(2):
        flag.forward(400)
        flag.right(90)
        flag.forward(200)
        flag.right(90)
    flag.end_fill()


# function to draw the border of the flag
def flag_border():
    """
    This function is for drawing the border of the flag colored in blue
    """
    # move the turtle to the correct position so that the center of the object will be the center of the screen
    border.penup()
    border.backward(200)
    border.left(90)
    border.forward(100)
    border.right(90)
    border.pendown()
    # loop for drawing a rectangle
    for i in range(2):
        border.forward(400)
        border.right(90)
        border.forward(200)
        border.right(90)


# functions to draw the star of the flag
# function to draw a triangle
def triangle():
    """
    This function is for drawing a white triangle for the star
    """
    star.begin_fill()
    # loop for drawing triangle
    for j in range(3):
        star.forward(70)
        star.left(120)
    star.end_fill()


def flag_star():
    """
    This function is for drawing a full star using triangle() function twice
    """
    # position the turtle for first triangle
    star.penup()
    star.backward(35)
    star.right(90)
    star.forward(20)
    star.left(90)
    star.pendown()
    triangle()
    # position the turtle for second triangle
    star.penup()
    star.left(90)
    star.forward(40)
    star.right(150)
    star.pendown()
    triangle()


# main program
flag_bg()       # call the flag background function
flag_border()   # call the flag border function
flag_star()     # call the star function

win.exitonclick()  # exit when user click
