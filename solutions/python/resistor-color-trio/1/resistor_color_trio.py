"Function to determine the resistance value from the given colors."

colors_dict = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

def label(colors):
    """Determine the resistance value using the two first given colors.

    :param colors: list - the list of given colors.  
    :return: str - the resistance value in omhs.    
    """
    prefix = ""
    resistance_value = ((colors_dict[colors[0]] * 10) + (colors_dict[colors[1]])) * (10**(colors_dict[colors[2]]))

    if resistance_value > 0:
        if resistance_value % (10**9) == 0:
            prefix = "giga"
            resistance_value = resistance_value // 10**9
            
        if resistance_value % (10**6) == 0:
            prefix = "mega"
            resistance_value = resistance_value // 10**6
            
        if resistance_value % (10**3) == 0:
            prefix = "kilo"
            resistance_value = resistance_value // 10**3
    
    return f"{resistance_value} {prefix}ohms"