"Function to determine the RNA complement of a given DNA sequence."

def to_rna(dna_strand):
    """Determine the RNA complement of the given DNA.

    :param dna_strand: str - the given DNA.
    :return: str - the RNA complement of the given DNA.
    """
    rna_table = str.maketrans("GCTA", "CGAU")
    
    return dna_strand.translate(rna_table)