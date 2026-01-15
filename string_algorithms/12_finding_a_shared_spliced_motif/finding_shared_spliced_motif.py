with open("rosalind_lcsq.txt", "r") as file:
    content = file.read().strip()
    
raw_entries = content.split('>')[1:]
sequences = []

for entry in raw_entries:
    lines = entry.splitlines()
    sequence = "".join(lines[1:])
    sequences.append(sequence)

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
lcs_string = ""

while i > 0 and j > 0:
    if s[i - 1] == t[j - 1]:
        lcs_string += s[i - 1]
        i -= 1
        j -= 1
    elif dp_matrix[i - 1][j] > dp_matrix[i][j - 1]:
        i -= 1
    else:
        j -= 1

# started from the end, so reverse the string
print(lcs_string[::-1])