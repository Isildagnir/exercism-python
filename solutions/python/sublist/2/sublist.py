"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 3
SUPERLIST = 2
EQUAL = 1
UNEQUAL = 4

def sublist(list_one, list_two):
    """Determine the link between two list.

    :param list_one: list - the first list.
    :param list_two: list- the second list.
    :return: int - the link between them.
    """
    if list_one == list_two:
        return EQUAL
    for index in range(len(list_one) - len(list_two) + 1):
        if not list_two or list_two == list_one[index: index + len(list_two)]:
            return SUPERLIST
    for index in range(len(list_two) - len(list_one) + 1):
        if not list_one or list_one == list_two[index: index + len(list_one)]:
            return SUBLIST
    return UNEQUAL