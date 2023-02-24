# Set X, Y and Z to three values where X <=Y<=Z
# and check whether a triangle with lengths X, Y and Z
# is equilateral, isosceles or scalene or that no triangle
# can be formed.  For example, when X = 3, Y = 4 and Z = 4
# the code prints “A triangle of sides X = 3, Y = 4 and Z = 4
# is isosceles”.


# function for triangle type
def triangle_check(a, b, c):
    """

    :param a: first size of the triangle
    :param b: second size of the triangle
    :param c: third size of the triangle
    :return: type of the triangle
    """
    tri_type = ""
    if a == b == c:
        tri_type = "This is a equilateral triangle"
    elif (a == b != c) or (a == c != b) or (b == c != a):
        tri_type = "This is a isosceles triangle"
    elif (a + b <= c) or (a + c <= b) or (b + c <= a):
        tri_type = "This is not a triangle"
    else:
        tri_type = "This is a scalene triangle"
    return tri_type


# main program
# input from keyboard
print("Input X,Y and Z (X<=Y<=Z)")
x = int(input())
y = int(input())
z = int(input())

# print out result
print(triangle_check(x, y, z))


# solution
"""
# define global variables
x = 2
y = 2
z = 3
def triangle_type(a,b,c):
    '''
    :param a: this is the first side of triangle
    :param b: this is the second side of triangle
    :param c: this is the third side of triangle
    :return: the sum of all sides
    '''
    # check equilateral
    if a == b == c:
        print("equilateral")
    # check isosceles
    # note: use elif and != to have exclusive conditions
    elif a == b != c or b == c != a or a == c != b:
        print("isosceles")
    # # note: use if and no != if you want the "equilateral" triangle classified as
"isosceles" as well
    # if a == b or b == c or a == c:
    #     print("isosceles")
    else:
        print("scalene")
    # calculate the sum of all sides
    sum_sides = a + b + c
    return sum_sides

# always try to try /except
try:
    # check if this is a triangle or not
    if x+y>z and y+z>x and x+z>y:
        print("It's a triangle")
        # calling the function to check triangle type
        sum_sides = triangle_type(x, y, z)
        print("Sum of the sides are: " + str(sum_sides))
    else:
        print("Not a triangle")
except Exception as e:
    print(e)
"""