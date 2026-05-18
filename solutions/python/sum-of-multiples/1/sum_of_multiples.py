"Function to calculate the energy points that a player get when they complete a level depending of the level and the value of each magical item the player collected."

def sum_of_multiples(limit, multiples):
    """Calculate the energy points.

    :param limit: int - the level that the player colpleted.
    :param multiples: list - the list of the base value of each item.
    :return: int - the energy points.
    """
    return sum(set(value*factor for factor in range(limit) for value in multiples if value*factor < limit))
