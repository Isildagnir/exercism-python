"Function to unpack nested array of any depth into a flattened array."

def flatten(iterable):
    """Unpack the nested array.

    :param iterable: list - the nested array.
    :return: list - the flattened array.
    """
    flattened_array= []
    
    for sublist in iterable:
        if sublist is None:
            continue
        if isinstance(sublist, list) :
            flattened_array.extend(flatten(sublist))
        else:
            flattened_array.append(sublist)

    return flattened_array