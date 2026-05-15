"function to determine what Bob whould reply to someone"

def response(hey_bob):
    """determine how Bob would answer a question or a statement.

    :param: str - the message adressed to Bob
    :return: str - Bob's response
    """
    if hey_bob.strip().endswith("?") and not hey_bob.isupper():
        return f"Sure."
    elif not hey_bob.strip().endswith("?") and hey_bob.isupper() :
        return f"Whoa, chill out!"
    elif hey_bob.strip().endswith("?") and hey_bob.isupper() :
        return f"Calm down, I know what I'm doing!"
    elif len(hey_bob) == 0 or hey_bob.isspace():
        return f"Fine. Be that way!"
    else:
        return f"Whatever."