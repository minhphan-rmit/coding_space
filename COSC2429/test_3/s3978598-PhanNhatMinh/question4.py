# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: Assignment 4 - Test 3
# Author: Phan Nhat Minh (s3978598)
# Created date: 14/01/2023
# Last modified date: 14/01/2023
# IDE: Pycharm 2022.2.3 (Professional Edition)
# Python version: 3.11
# Question: 4


# class
class MyPoint:
    """A class to model three-dimensional space"""

    def __init__(self, x, y, z):
        """Initialize x, y, and z attributes"""
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """Represents the point when print function is called"""
        return "(%s, %s, %s)" % (self.x, self.y, self.z)

    def __add__(self, otherPoint):
        """Concatenate points"""
        return MyPoint(self.x + otherPoint.x, self.y + otherPoint.y, self.z + otherPoint.z)


# main program
# given points
p1 = MyPoint(1, 2, 3)
p2 = MyPoint(2, 3, 4)
# print out points
print(p1)
print(p2)
# new point that is a sum of two given points
p3 = p1 + p2
# print out the new points
print(p3)
