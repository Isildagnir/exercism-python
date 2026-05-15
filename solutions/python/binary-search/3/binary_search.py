"Function to implement the binary search algorithm."

def find(search_list, value):
    """Implement the binary search algorithm

    :param search_list: list - the given list needed to be searched.
    :param value: int - the given seached value.
    :return: int - the index where the given value is in the list.
    """
    sorted_list = sorted(search_list)
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        medium = (low + high) // 2
        if sorted_list[medium] == value:
            return medium
            
        if sorted_list[medium] > value:
            high = medium - 1
                
        else:
            low = medium + 1
                
    raise ValueError("value not in array")