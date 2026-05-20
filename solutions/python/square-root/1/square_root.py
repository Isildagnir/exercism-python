"Function to calculate the square root of a given number without math module."

def square_root(number):
    """Calculate the square root.

    :param number: int - the given number.
    :return: int - the square root of this number.
    """
    if number == 1:
        return number
    for digit in range((number//2) + 1):
        if digit*digit == number:
            return digit