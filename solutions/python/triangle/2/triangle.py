"""Functions for determining the properties of a triangle based on its sides"""

def is_triangle(sides):
    """determine if the given sides draw a triangle.

    :param: list[int] - list of sides.
    :return: bool - True if this is a triangle and False if not.

    """
    if len(sides) >= 4:
        return False
    
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]
    
    return (((side_a + side_b) >= side_c) and ((side_b + side_c) >= side_a) and ((side_a + side_c) >= side_b)) and (side_a > 0 and side_b > 0 and side_c > 0)
    
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
        return not isosceles(sides)
    return False
