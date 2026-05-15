"""Functions for determining the properties of a triangle based on its sides"""

def is_triangle(sides):
    """determine if the given sides draw a triangle.

    :param: list[int] - list of sides.
    :return: bool - True if this is a triangle and False if not.

    """
    if len(sides) >= 4:
        return False
    
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    return (((a + b) >= c) and ((b + c) >= a) and ((a + c) >= b)) and (a > 0 and b > 0 and c > 0)
    
def equilateral(sides):
    """determine if the triangle is equilateral.

    :param: list[int] - list of sides.
    :return: bool - True if the triangle is equilateral and False if not.

    """
    if is_triangle(sides):
        return sides[0] == sides[1] and sides[1] == sides[2] and sides[0] == sides[2]
    return False

def isosceles(sides):
    """determine if the triangle is isosceles.

    :param: list[int] - list of sides.
    :return: bool - True if the triangle is isosceles and False if not.

    """
    if is_triangle(sides):
        return equilateral(sides) or (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])
    return False

def scalene(sides):
    """determine if the triangle is scalene.

    :param: list[int] - list of sides.
    :return: bool - True if the triangle is scalene and False if not.

    """
    if is_triangle(sides):
        return not(isosceles(sides))
    return False
