"function to calculate the points scored in a single toss of a Dartes game"

def score(x, y):
    """Calculate the points scored in the Darts game.

    :param: int / float or complex - the coordinate x of the point in the target.
    :param: int / float or complex - the coordinate y of the point in the target.
    :return: int - the points scored by the player.
    
    """
    points_scored = 0
    circle_equation = (x**2) + (y**2)
    
    if 5**2 < circle_equation <= 10**2:
        points_scored = 1
    if 1 < circle_equation <= 5**2:
        points_scored = 5
    if 0 <= circle_equation <= 1:
        points_scored = 10
    return points_scored
