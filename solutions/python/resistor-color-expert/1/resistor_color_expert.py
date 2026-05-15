"Function to determine the resistance value and the tolerance of a resistor."

colors_resistance_dict = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
colors_tolerance_dict = {"grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5, "brown": 1, "red": 2, "gold": 5, "silver": 10}

def resistor_label(colors):
    """Determine the resistance value and tolerance of the given colors.
    
    :param colors: list - the list of given colors.
    :return: str - the resistance value in ohms.
    """
    resistance_value = 0
    tolerance_value = 0
    prefix = ""
    
    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        resistance_value = ((colors_resistance_dict[colors[0]] * 10) + (colors_resistance_dict[colors[1]])) * (10**(colors_resistance_dict[colors[2]]))
        tolerance_value = colors_tolerance_dict[colors[3]]
        
    if len(colors) == 5:
        resistance_value = ((colors_resistance_dict[colors[0]] * 100) + (colors_resistance_dict[colors[1]] * 10) + (colors_resistance_dict[colors[2]])) * (10**(colors_resistance_dict[colors[3]]))
        tolerance_value = colors_tolerance_dict[colors[4]]

    if resistance_value > 0:
        if resistance_value >= (10**9):
            prefix = "giga"          
            resistance_value = resistance_value / 10**9 if resistance_value%10**9 != 0 else resistance_value // 10**9 

        if resistance_value >= (10**6):
            prefix = "mega"          
            resistance_value = resistance_value / 10**6 if resistance_value%10**6 != 0 else resistance_value // 10**6 

        if resistance_value >= (10**3):
            prefix = "kilo"          
            resistance_value = resistance_value / 10**3 if resistance_value%10**3 != 0 else resistance_value // 10**3 

    return f"{resistance_value} {prefix}ohms ±{tolerance_value}%"