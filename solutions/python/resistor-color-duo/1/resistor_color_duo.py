"Function to determine the resistance value from the given colors."

colors_dict = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

def value(colors):
    """Determine the resistance value using the two first given colors.

    :param colors: list - the list of given colors.
    :return: int - the resistance value.
    """
    return (colors_dict[colors[0]] * 10) + (colors_dict[colors[1]])