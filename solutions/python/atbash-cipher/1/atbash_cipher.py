"Fucntion to implement the Atbash cipher."

def encode(plain_text):
    """Encode the given text with the Atbash cipher.

    :param plain_text: str - the given text.
    :return: str - the given text with the Atbash cipher applied.
    """
    ciphered_text = ""
    group_length = 0

    for word in plain_text.lower():
        for letter in word:
            if letter.isalpha():
                if group_length == 5:
                    ciphered_text += " "
                    group_length = 0
                ciphered_text += chr(ord("a") + (25 - (ord(letter) - ord("a")))).lower()
                group_length += 1
                    
            if letter.isnumeric():
                if group_length == 5:
                        ciphered_text += " "
                        group_length = 0
                ciphered_text += letter
                group_length += 1
                
    return ciphered_text

def decode(ciphered_text):
    """Decode the given text with the Atbash cipher.

    :param ciphered_text: str - the given ciphered text.
    :return: str - the given text without the Atbash cipher.
    """
    plain_text = ""

    for word in ciphered_text.split():
        for letter in word:
            if letter.isalpha():
                plain_text += chr(ord("a") + (25 - (ord(letter) - ord("a"))))
            else:
                plain_text += letter
    return plain_text