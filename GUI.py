import PySimpleGUI as psg
from subdir.dna_utils import count_nucleotides, transcribe_dna_to_rna
from subdir.translation_utils import translate_rna_to_amino_acids
from subdir.error_handler import validate_dna_sequence


def process_dna_sequence(dna):
    try:
        # Validate the DNA sequence
        validate_dna_sequence(dna)

        print("\n--- DNA Operations ---")
        print("DNA Sequence:", dna)

        # Count nucleotides
        nucleotide_counts = count_nucleotides(dna)
        print("Nucleotide counts:", nucleotide_counts)

        # Transcribe DNA to RNA
        rna = transcribe_dna_to_rna(dna)
        print("mRNA Sequence:", rna)

        # Translate RNA to amino acids
        amino_acids = translate_rna_to_amino_acids(rna)
        print("Amino Acids:", amino_acids)

    except ValueError as e:
        print("Error:", str(e))


# GUI Layout
layout = [
    [psg.Text('DNA Translation', font=('Arial', 20), justification='center')],
    [psg.Text('Enter DNA Sequence:', font=('Arial', 12))],
    [psg.InputText(key='dna_input')],
    [psg.Button('Translate', size=(10, 1), font=('Arial', 12))],
    [psg.Text('Output:', font=('Arial', 12))],
    [psg.Output(size=(60, 10), font=('Arial', 12))]
]

# Create the window
window = psg.Window('DNA Translation', layout, element_justification='center')

# Event loop to process GUI events
while True:
    event, values = window.read()

    # Break the loop if the window is closed
    if event == psg.WINDOW_CLOSED:
        break

    # Translate button
    if event == 'Translate':
        dna_sequence = values['dna_input']
        process_dna_sequence(dna_sequence)

# Close the window
window.close()
