"Function to generate a sentence with the name and the number in file from a customer."

ordinal_dict = {"1":"st", "2":"nd", "3":"rd"}

def line_up(name, number):
    """Generate the sentence.

    :param name: str - the customer's name.
    :param number: int - the number in file.
    :return: str - the sentence generate using the customer's name and numer in file.
    """
    if number > len(ordinal_dict) and ((str(number)[-1] not in ordinal_dict) or (len(str(number)) > 1 and str(number)[-2] == "1")):
        ordinal = "th"
    else:
        ordinal = ordinal_dict[str(number)[-1]]
        
    return f"{name}, you are the {number}{ordinal} customer we serve today. Thank you!"