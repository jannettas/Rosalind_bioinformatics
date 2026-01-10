rna_to_protein = {
	'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
	'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
	'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
	'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
	'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
	'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
	'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
	'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
	'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
	'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
	'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
	'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
	'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
	'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
	'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
	'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}

with open("rosalind_splc.txt", "r") as f:
	raw_data = f.read().split(">")
	# remove the first empty element
	raw_data = raw_data[1:]
sequences = {}
for entry in raw_data:
	lines = entry.splitlines()
	label = lines[0]
	sequence = "".join(lines[1:])
	sequences[label] = sequence

# remove non-coding introns, keep only exons
dna = list(sequences.values())[0]
introns = list(sequences.values())[1:]
for intron in introns:
	dna = dna.replace(intron, "")

# DNA -> RNA
rna_seq = dna.replace("T", "U")

# RNA -> Protein
protein = ""
for i in range(0, len(rna_seq), 3):
    codon = rna_seq[i:i+3]
    if rna_to_protein[codon] == 'Stop':
        break
    protein += rna_to_protein[codon]
print(protein)