"Function to calculate the number of steps required to reach '1' with the Collatz Conjecture."

def steps(number):
    """calculate the steps to reach '1' with the Collatz Conjecture.

    :param: int - the given positive number.
    :return: int - the number of steps needed.
    
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    number_of_steps = 0

    while number != 1:
        if (number % 2) == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        number_of_steps += 1
        
    return number_of_steps