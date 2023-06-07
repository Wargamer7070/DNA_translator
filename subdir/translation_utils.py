amino_acid_table = {
    'UUU': ('Phe', 'Phenylalanine'),
    'UUC': ('Phe', 'Phenylalanine'),
    'UUA': ('Leu', 'Leucine'),
    'UUG': ('Leu', 'Leucine'),
    'CUU': ('Leu', 'Leucine'),
    'CUC': ('Leu', 'Leucine'),
    'CUA': ('Leu', 'Leucine'),
    'CUG': ('Leu', 'Leucine'),
    'AUU': ('Ile', 'Isoleucine'),
    'AUC': ('Ile', 'Isoleucine'),
    'AUA': ('Ile', 'Isoleucine'),
    'AUG': ('Met', 'Methionine'),
    'GUU': ('Val', 'Valine'),
    'GUC': ('Val', 'Valine'),
    'GUA': ('Val', 'Valine'),
    'GUG': ('Val', 'Valine'),
    'UCU': ('Ser', 'Serine'),
    'UCC': ('Ser', 'Serine'),
    'UCA': ('Ser', 'Serine'),
    'UCG': ('Ser', 'Serine'),
    'CCU': ('Pro', 'Proline'),
    'CCC': ('Pro', 'Proline'),
    'CCA': ('Pro', 'Proline'),
    'CCG': ('Pro', 'Proline'),
    'ACU': ('Thr', 'Threonine'),
    'ACC': ('Thr', 'Threonine'),
    'ACA': ('Thr', 'Threonine'),
    'ACG': ('Thr', 'Threonine'),
    'GCU': ('Ala', 'Alanine'),
    'GCC': ('Ala', 'Alanine'),
    'GCA': ('Ala', 'Alanine'),
    'GCG': ('Ala', 'Alanine'),
    'UAU': ('Tyr', 'Tyrosine'),
    'UAC': ('Tyr', 'Tyrosine'),
    'UAA': ('Stop', 'Stop'),
    'UAG': ('Stop', 'Stop'),
    'CAU': ('His', 'Histidine'),
    'CAC': ('His', 'Histidine'),
    'CAA': ('Gln', 'Glutamine'),
    'CAG': ('Gln', 'Glutamine'),
    'AAU': ('Asn', 'Asparagine'),
    'AAC': ('Asn', 'Asparagine'),
    'AAA': ('Lys', 'Lysine'),
    'AAG': ('Lys', 'Lysine'),
    'GAU': ('Asp', 'Aspartic Acid'),
    'GAC': ('Asp', 'Aspartic Acid'),
    'GAA': ('Glu', 'Glutamic Acid'),
    'GAG': ('Glu', 'Glutamic Acid'),
    'UGU': ('Cys', 'Cysteine'),
    'UGC': ('Cys', 'Cysteine'),
    'UGG': ('Trp', 'Tryptophan'),
    'CGU': ('Arg', 'Arginine'),
    'CGC': ('Arg', 'Arginine'),
    'CGA': ('Arg', 'Arginine'),
    'CGG': ('Arg', 'Arginine'),
    'AGU': ('Ser', 'Serine'),
    'AGC': ('Ser', 'Serine'),
    'AGA': ('Arg', 'Arginine'),
    'AGG': ('Arg', 'Arginine'),
    'GGU': ('Gly', 'Glycine'),
    'GGC': ('Gly', 'Glycine'),
    'GGA': ('Gly', 'Glycine'),
    'GGG': ('Gly', 'Glycine')
}

def translate_rna_to_amino_acids(rna_string):
    codons = [rna_string[i:i+3] for i in range(0, len(rna_string), 3)]
    amino_acids = []
    full_names = []
    for codon in codons:
        if codon in amino_acid_table:
            amino_acid, full_name = amino_acid_table[codon]
            if amino_acid == 'Stop':
                break
            amino_acids.append(amino_acid)
            full_names.append(full_name)
    return amino_acids, full_names
