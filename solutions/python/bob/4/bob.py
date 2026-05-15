"function to determine what Bob whould reply to someone"

def response(hey_bob):
    """determine how Bob would answer a question or a statement.

    :param: str - the message adressed to Bob
    :return: str - Bob's response
    """
    if hey_bob.strip().endswith("?") and not hey_bob.isupper():
        return "Sure."
    if hey_bob.isupper() :
        if hey_bob.strip().endswith("?"):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if len(hey_bob) == 0 or hey_bob.isspace():
        return "Fine. Be that way!"
    return "Whatever."