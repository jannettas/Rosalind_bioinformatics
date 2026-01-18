with open("rosalind_cons.txt", "r") as file:
    lines = file.readlines()

dna_strings = []
current_dna = ""

for line in lines:
    line = line.strip()

    if line.startswith(">"):
        # if we encounter a header and have accumulated DNA, save it
        if current_dna != "":
            dna_strings.append(current_dna)
            current_dna = "" # Reset for the next sequence
    else:
        # if this is not a header, it is a piece of DNA so we add it to the current sequence
        current_dna += line

#  add the last sequence after the loop
if current_dna != "":
    dna_strings.append(current_dna)
    
#print(dna_strings)

n = len(dna_strings[0])

# dictionary with bases counters
profile = {
    'A': [0] * n,
    'C': [0] * n,
    'G': [0] * n,
    'T': [0] * n
}

for dna in dna_strings:
    for i in range(n):
        nucleotide = dna[i]
        profile[nucleotide][i] += 1

#print("A:", profile['A'])
#print("C:", profile['C'])
#print("G:", profile['G'])
#print("T:", profile['T'])

consensus_string = ""

for i in range(n):
    max_count = -1
    max_nucleotide = ""

    for nucleotide in ['A', 'C', 'G', 'T']:
        count = profile[nucleotide][i]
        if count > max_count:
            max_count = count
            max_nucleotide = nucleotide
	# add the base to consensus string
    consensus_string += max_nucleotide

print(consensus_string)

# print matrix
for nucleotide in ['A', 'C', 'G', 'T']:
    # turn list of counts into string
    counts_str = ' '.join(map(str, profile[nucleotide]))
    print(f"{nucleotide}: {counts_str}")