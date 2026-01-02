with open("rosalind_hamm.txt") as f:
	full_sequence = "".join(f.read().split())

	half = len(full_sequence) // 2
	str1 = full_sequence[:half]
	str2 = full_sequence[half:]

i = 0
count = 0

while (i < half):
	if (str1[i] != str2[i]):
		count += 1
	i += 1
# more pythonic version in one line
# count = sum(1 for a, b in zip(str1, str2) if a != b)

print(count)