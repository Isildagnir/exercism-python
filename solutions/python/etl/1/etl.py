"Function to transform the data format of the game."

def transform(legacy_data):
    """Transform the legacy_data with the new format.

    :param legacy_data: dict - the dict of the legacy format.
    :return: dict - the dict with the new format.
    """
    dict_new_format = {}
    
    for key in legacy_data.keys():
        for value in legacy_data[key]:
            dict_new_format.setdefault(value.lower(), key)
    return dict_new_format