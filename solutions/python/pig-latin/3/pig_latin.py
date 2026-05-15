"Function to translate a text from English to Pig Latin "

def translate(text):
    """ translate English text to Pig Latin.

    :param text: str - the given text in English
    :return: str - the given text translated in Pig Latin
    """
    vowels = ("a", "e", "i", "o", "u")
    cut_position = 0
    translated_text = []

    for index_text, word in enumerate(text.split()):
        if (word[0],word[1]) != ("x", "r") and (word[0],word[1]) != ("y", "t"):
            for index, letter in enumerate(word):
                if letter in vowels or (letter, word[index + 1]) == ("q", "u"):
                    cut_position = index
                    break
                if word[index + 1] == "y":
                    cut_position = index + 1
                    break
        if word[cut_position] == "q":
            translated_text.append(word[cut_position + 2:] + word[:cut_position + 2] + "ay")
        else:
            translated_text.append(word[cut_position:] + word[:cut_position] + "ay")
    return " ".join(translated_text)