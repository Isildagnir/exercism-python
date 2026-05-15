"Function to convert a text using rotational cipher."

def rotate(text, key):
    """convert the text with the given rotational key.

    :param text: str - the given text.
    :param key: int - the given key for the rotational cipher.
    :return: str - the translated text.
    """
    translated_text = []
    if key in {0, 26}:
        return text

    for word in text:
        for letter in word:
            if letter.isalpha():
                if letter.isupper():
                    translated_text.append(chr((ord(letter) + key - ord("A")) % 26 + ord("A")))
                    
                else:
                    translated_text.append(chr((ord(letter) + key - ord("a")) % 26 + ord("a")))
            else:
                translated_text.append(letter)
                
    return "".join(translated_text)