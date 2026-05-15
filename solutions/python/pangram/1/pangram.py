import string

" function to determine if a sentence is a pangram, i.e. a sentence using every letter of the alphabet at least once"

def is_pangram(sentence):
    """determine if a sentence is a pangram
    
    :param sentence: str - the given sentence
    :return: bool - True if this is a pangram, False if not"""
    alphabet = list(string.ascii_lowercase)
    for letter in sentence.casefold():
        if letter in alphabet:
            alphabet.remove(letter)
    return alphabet == []
