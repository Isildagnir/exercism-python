"function to determine if a string is a valid ISBN"

def is_valid(isbn):
    """determine if the given string is ISBN-10.

    :param isbn: str - the given string.
    :return: bool - True if it's a valid ISBN-10, False if not.
    """
    testing_isbn = isbn.replace("-","").lower()
    sum_formula = 0
    valid_char = [str(number) for number in range(10)] + ["x"]

    if len(testing_isbn) != 10:
        return False

    for index, digit in enumerate(reversed(testing_isbn)):
        if digit not in valid_char:
            return False
        if digit == "x":
            if index == 0:
                sum_formula += 10*(index + 1)
                continue
            return False
            
        sum_formula += int(digit)*(index + 1)
        
    return (sum_formula % 11) == 0