"Function to determine the date and the time one gigasecond after a certain date."

from datetime import timedelta

def add(moment):
    """Calcultate the date and the hour after one gigasecond given a certain date.

    :param moment: datetime - the given date.
    :return: datetime - the date and hour after one gigasecond.
    """
    return moment + timedelta(seconds = 1e9)