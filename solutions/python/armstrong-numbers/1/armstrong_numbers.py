"Function to determine if a number is an armstrong number"

def is_armstrong_number(number):
    """determine if the number is armstrong.

    :param: int - the given number.
    :return: bool - True if this is a armstrong number, False if not.
    
    """
    list_digits = list(map(int, str(number)))
    sum_digits = 0
    
    for digit in list_digits:
        sum_digits += digit**(len(list_digits))
    if sum_digits == number:
        return True
    return False
    
