def validate_dna_sequence(sequence):
    # Check if the sequence contains only valid characters (A, T, G, C)
    valid_characters = {'A', 'T', 'G', 'C'}
    if not set(sequence).issubset(valid_characters):
        raise ValueError("Invalid DNA sequence. It should only contain the characters A, T, G, C.")

    # Check if the sequence length is a multiple of 3
    if len(sequence) % 3 != 0:
        raise ValueError("Invalid DNA sequence length. It should be a multiple of 3.")


def validate_amino_acid_sequence(sequence):
    # Check if the sequence contains only valid amino acids
    valid_amino_acids = {'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'}
    if not set(sequence).issubset(valid_amino_acids):
        raise ValueError("Invalid amino acid sequence. It contains invalid characters.")

    # Check if the sequence length is a multiple of 3
    if len(sequence) % 3 != 0:
        raise ValueError("Invalid amino acid sequence length. It should be a multiple of 3.")
