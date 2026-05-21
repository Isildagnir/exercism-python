"Function to determine if brackets, braces, parentheses or any combination is are matched."

import string

def is_paired(input_string):
    """Determine if all pairs are matched and nested correctly.

    :param input_string: str - the given string.
    :return: bool - True if all pairs are matched, False if not.
    """
    testing_string = input_string.replace(string.ascii_letters, "")
    opened = "[{("
    closed = "]})"
    track = []
    
    for item in testing_string:
        if item in opened:
            track.append(item)
        if item in closed:
            if not track or opened[closed.index(item)] != track.pop():
                return False
    return not track