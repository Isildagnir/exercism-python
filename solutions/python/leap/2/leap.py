"""Function to give if a year is a leap year"""

def leap_year(year):
    """give if a year is a leap year.

    :param year: int - the given year
    :return: bool - true if the year is a leap year, false if not

    """
    if (year % 4) == 0:
        if (year % 100) == 0:
            return (year % 400) == 0
        return True
    return False
