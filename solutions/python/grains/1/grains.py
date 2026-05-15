"""Functions for determining the properties of a triangle based on its sides"""

def square(number):
    """calculate the number of grains on a given square of the chessboard.

    :param: int - the given square.
    :return: int - the number of grains.

    """
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    return 1 * (2**(number - 1))


def total():
    """calculate the total number of grains on the chessboard.

    :return: int - the number of grains on the chessboard.

    """
    return ((2**64) - 1) // (2 - 1)
    
