"Functions to determine the difference between the square of the sum and the sum of the squares of the first N natural numbers."

def square_of_sum(number):
    """Calculate the square of sum.

    :param number: int - the limit for the sum.
    :return: int - the square of sum of the numbers.
    """
    return sum(digit for digit in range(number + 1))**2


def sum_of_squares(number):
    """Calculate the sum of squares.

    :param number: int - the limit for the sum.
    :return: int - the sum of squares of the numbers.
    """
    return sum(digit**2 for digit in range(number + 1))


def difference_of_squares(number):
    """Calculate the difference between the square of the sum and the sum of the squares.

    :param number: int - the limit for the sum.
    :return: int - the difference between the square of the sum and the sum of the squares.
    """
    return square_of_sum(number) - sum_of_squares(number)
