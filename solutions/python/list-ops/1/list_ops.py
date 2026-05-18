"Functions to implement basic list operations"

def append(list1, list2):
    """Add all items from the second list to the first one.

    :param list1: list - the first list.
    :param list2: list - the second list.
    :return: list - the first list with the added items of the second list.
    """
    return list1 + list2


def concat(lists):
    """Add all items from the all list into one list.

    :param lists: list - the lists of list.
    :return: list - the concatened list.
    """
    concatened = []
    for list in lists:
        concatened += list
    return concatened

def filter(function, list):
    """Return all items from the list for which the condittion "the predicate(item) is True" is satisfied.

    :param function: func - the condition to satisfied.
    :param list: list - the list.
    :return: list - the list of items which satisfied the condition.
    """
    filtered = []
    for item in list:
        if function(item):
            filtered += [item]
    return filtered
    
def length(list):
    """Calculate the length of a list.

    :param list: list - the list.
    :return: int - the length of the list.
    """
    return sum(1 for item in list) if list else 0

def map(function, list):
    """Apply the given function to all items from the list.

    :param function: func - the function to apply.
    :param list: list - the list.
    :return: list - the list in wich the function has been applied to each item.
    """
    return [function(item) for item in list]


def foldl(function, list, initial):
    """Apply the function to all item with the accumulator from left to right of the list.

    :param function: func - the function to apply.
    :param list: list - the list.
    :param initial: type from item of the list - the initial accumulator
    :return: type from item of the list - the final accumulator
    """
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc

def foldr(function, list, initial):
    """Apply the function to all item with the accumulator from right to left of the list.

    :param function: func - the function to apply.
    :param list: list - the list.
    :param initial: type from item of the list - the initial accumulator
    :return: type from item of the list - the final accumulator
    """
    acc = initial
    
    for item in reverse(list):
        acc = function(acc, item)
    return acc

def reverse(list):
    """Reverse the order of the items of the list.

    :param list: list - the list.
    :return: list - the reversed list.
    """
    return [list[index] for index in range(length(list) - 1, -1, -1)]
