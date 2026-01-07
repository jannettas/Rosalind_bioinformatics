codon_counts = {
    'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2,
    'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4,
    'A': 4, 'D': 2, 'E': 2, 'G': 4
}

MODULO_VALUE = 1000000

with open('rosalind_mrna.txt', 'r') as file:
    protein_string = file.read().strip()

# starting value 3 for one of 3 stop codons in the end of string(UAG, UGA, UAA)
total_variants = 3

for amino_acid in protein_string:
    # get codon count for the amino acid
    count = codon_counts[amino_acid]
    # apply modulo to prevent overflow
    total_variants = (total_variants * count) % MODULO_VALUE

print(total_variants)