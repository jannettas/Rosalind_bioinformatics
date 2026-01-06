sequences = []
current_seq = ""

with open("rosalind_lcsm.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            if current_seq: 
                sequences.append(current_seq)
            current_seq = ""
        else:
            current_seq += line
    # add the last sequence after the loop ends and there is no next ">" line
    if current_seq:
        sequences.append(current_seq)
        
short_seq = min(sequences, key=len)
n = len(short_seq)
result = ""

# outer loop checks which length of substring we are testing
for length in range(n, 0, -1):
    # inner loop goes through all substrings of this length
    for start in range(n - length + 1):
        motif = short_seq[start : start + length]
        # checking if this motif is in all sequences
        if all(motif in s for s in sequences):
            result = motif
            break     
    if result: 
        break # If we found something at this length, it's the max, stop here
print(result)	