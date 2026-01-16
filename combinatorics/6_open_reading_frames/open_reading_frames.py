dna_codon_table = {
	'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
	'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
	'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
	'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
	'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
	'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
	'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
	'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
	'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
	'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
	'TAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
	'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
	'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
	'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
	'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
	'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }

with open("rosalind_orf.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    s = "".join(lines[1:])
    
    complement_map = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    # reverse the string and swap bases
    rev_s = "".join(complement_map[base] for base in s[::-1])

    # find ORFs in s and rev_s
    results = set()
    for strand in [s, rev_s]:
        # look for a start codon position
        for i in range(len(strand) - 2):
            if strand[i:i+3] == 'ATG':
                protein = ''
                found_stop = False

                # start translating from this position
                for j in range(i, len(strand) - 2, 3):
                    codon = strand[j:j+3]
                    amino = dna_codon_table.get(codon, '')

                    if amino == 'Stop':
                        found_stop = True
                        break

                    protein += amino
                # add protein if we found stop codon
                if found_stop:
                    results.add(protein)

    for p in results:
        print(p)