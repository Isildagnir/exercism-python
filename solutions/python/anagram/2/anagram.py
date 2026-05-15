"Function to determine in a given list wich word are anagram of the given word."

def find_anagrams(word, candidates):
    """Finding the anagrams of the given word.

    :param word: str - the given word.
    :param candidates: str - the list of potential anagram.
    :return: list - the list of anagram included in the candidates list.
    """
    return [candidate for candidate in candidates if candidate.lower() != word.lower() and sorted(candidate.lower()) == sorted(word.lower())]