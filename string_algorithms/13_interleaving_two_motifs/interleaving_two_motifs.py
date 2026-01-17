with open("rosalind_scsp.txt", "r") as file:
    sequences = [line.strip() for line in file if line.strip()]

s = sequences[0]
t = sequences[1]

m = len(s)
n = len(t)

# create a matrix filled with zeros, dimensions: (m+1) rows x (n+1) columns
dp_matrix = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
	for j in range(1, n + 1):
		if s[i - 1] == t[j - 1]:
			dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
		else:
			dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i][j - 1])

# backtracking
i, j = m, n
scs_string = ""

while i > 0 and j > 0:
    if s[i - 1] == t[j - 1]:
        scs_string += s[i - 1]
        i -= 1
        j -= 1
    elif dp_matrix[i - 1][j] > dp_matrix[i][j - 1]:
        # moving up, s[i-1] is part of supersequence but not the common one, so add it
        scs_string += s[i - 1]
        i -= 1
    else:
        # moving left, t[j-1] is part of supersequence
        scs_string += t[j - 1]
        j -= 1

# add remaining characters if we hit the edge (i=0 or j=0)
while i > 0:
    scs_string += s[i - 1]
    i -= 1
while j > 0:
    scs_string += t[j - 1]
    j -= 1

# reverse string 
print(scs_string[::-1])