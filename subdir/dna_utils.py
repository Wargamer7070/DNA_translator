def count_nucleotides(dna_string):
    nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in dna_string:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1
    return nucleotide_counts


def transcribe_dna_to_rna(dna_string):
    rna_string = ''
    for nucleotide in dna_string:
        if nucleotide in codon_table:
            rna_string += codon_table[nucleotide]
    return rna_string


codon_table = {
    'A': 'U',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}
