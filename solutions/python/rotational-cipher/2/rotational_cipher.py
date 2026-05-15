"Function to convert a text using rotational cipher."
import string

def rotate(text, key):
    """convert the text with the given rotational key.

    :param text: str - the given text.
    :param key: int - the given key for the rotational cipher.
    :return: str - the translated text.
    """
    translated_text = []
    if key in (0, 26):
        return text

    for word in text:
        for letter in word:
            if letter in string.ascii_letters:
                if letter.isupper():
                    if (ord(letter) + key) > ord("Z"):
                        translated_text.append(chr((ord("a") - 1) + ((ord(letter) + key) - ord("z"))))
                    else:
                        
                        translated_text.append(chr(ord(letter) + key))
                else:
                    if (ord(letter) + key) > ord("z"):
                        translated_text.append(chr((ord("a") - 1) + ((ord(letter) + key) - ord("z"))))
                    else: 
                        translated_text.append(chr(ord(letter) + key))
            else:
                translated_text.append(letter)
                
    return "".join(translated_text)