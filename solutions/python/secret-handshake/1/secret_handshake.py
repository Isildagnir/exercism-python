"Function to determine what actions you need to do based on the given number in binary"

actions = ["wink", "double blink", "close your eyes", "jump"]

def commands(binary_str):
    """Determine actions to make based on the given number.

    :param binary_str: str - the given number in binary.
    :return: str - the actions for the secret handshake.
    """
    secret_handshake = []
    
    for index, digit in enumerate(reversed(binary_str)):
        if digit == "1" and index < len(actions):
            secret_handshake.append(actions[index])
            
    if binary_str[0] == "1" and len(binary_str) > len(actions):
        return list(reversed(secret_handshake))
    return secret_handshake