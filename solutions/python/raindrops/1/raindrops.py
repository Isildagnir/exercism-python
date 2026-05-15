"Function to determine the raindrop sounds of a number"

def convert(number):
    """ determine the raindrop sound.

    :param: int - the given number.
    :return: str - the raindrop sound or the number if not divisible by 3, 5 or 7.
    
    """
    raindrop_sound = ""

    if (number % 3) == 0:
        raindrop_sound += "Pling"
    if (number % 5) == 0:
        raindrop_sound += "Plang"
    if (number % 7) == 0:
        raindrop_sound += "Plong"
    if raindrop_sound == "":
        raindrop_sound += f"{number}"
    return raindrop_sound