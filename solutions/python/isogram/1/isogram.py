"Function to dertemine if a word/sentence is an isogram, i.e. without having a repeating letter."

def is_isogram(string):
    """Determine if a word/sentence is an isogram.

    :param sting: str - the given word or sentence.
    :return: bool - True if it is an isogram, False if not. 
    """
    testing_string = "".join(word.strip(" -") for word in string).lower()
    
    for letter in testing_string:
        if testing_string.count(letter) > 1 :
            return False
    return True