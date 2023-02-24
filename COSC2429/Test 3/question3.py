# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022B
# Assignment: 4 - Final test
# Author: Kim Minsung (s3866724)
# Created date: 17/09/2022
# Last modified date: 17/09/2022

class Motorcycle(object):

    def __init__(self, brand, color, mileage):
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def print(self):
        print(f'The {self.brand} {self.color} motorcycle has {self.mileage:,} miles.')


honda = Motorcycle("Honda", "blue", 20000)
yamaha = Motorcycle("Yamaha", "red", 30000)

honda.print()
yamaha.print()
