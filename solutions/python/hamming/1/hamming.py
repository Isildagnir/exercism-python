"Function to calculate the Hamming distance, i.e. the numbers of incorrects informations during the division process."

def distance(strand_a, strand_b):
    """Calculate the Hamming distance.

    :param strand_a: str - the DNA before the cell division.
    :param strand_b: str - the DNA after the cell division.
    :return: int - the Hamming distance.
    """
    hamming_distance = 0

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    for index, nucleotide in enumerate(strand_a):
        if nucleotide != strand_b[index]:
            hamming_distance += 1

    return hamming_distance