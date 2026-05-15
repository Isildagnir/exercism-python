"Funcions to determine the colors use for resistors and their values."

colors_dict = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

def color_code(color):
    """Determine the resistance value of a given color.

    :param color: str - the given color.
    :return: int - the resistance value of the given color.
    """
    return colors_dict[color]


def colors():
    return list(colors_dict.keys())
