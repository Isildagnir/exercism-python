"function to determine what Bob whould reply to someone"

def response(hey_bob):
    """determine how Bob would answer a question or a statement.

    :param: str - the message adressed to Bob
    :return: str - Bob's response
    """
    if hey_bob.strip().endswith("?") and not hey_bob.isupper():
        return "Sure."
    if not hey_bob.strip().endswith("?") and hey_bob.isupper() :
        return "Whoa, chill out!"
    if hey_bob.strip().endswith("?") and hey_bob.isupper() :
        return "Calm down, I know what I'm doing!"
    if len(hey_bob) == 0 or hey_bob.isspace():
        return "Fine. Be that way!"
    return "Whatever."