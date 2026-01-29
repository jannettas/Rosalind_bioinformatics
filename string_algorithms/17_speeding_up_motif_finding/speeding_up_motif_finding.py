# function to read FASTA file
def read_fasta(filename):
	with open(filename, "r") as file:
		lines = file.readlines()
		dna = "".join(line.strip() for line in lines if not line.startswith(">"))
	return dna

s = read_fasta("rosalind_kmp.txt")
n = len(s)

P = [0] * n
j = 0

for i in range(1, n):
    # go back to previous prefix len if symbols differ 
	while j > 0 and s[i] != s[j]:
		j = P[j-1]
    
    # if symbols match, += prefix len
	if s[i] == s[j]:
		j += 1
    
	P[i] = j
	#print(P[i], end=" ")
    
with open('output.txt', 'w') as file:
	file.write(" ".join(map(str, P)))