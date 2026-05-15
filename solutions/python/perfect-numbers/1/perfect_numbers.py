"Function to determine the category of a number based of nicomachus classification based on their aliquot sum."

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
        
    factors = [factor for factor in range(1, (number//2) + 1) if number % factor == 0]

    if number == sum(factors):
        return "perfect"
    if number < sum(factors):
        return "abundant"
    return "deficient"