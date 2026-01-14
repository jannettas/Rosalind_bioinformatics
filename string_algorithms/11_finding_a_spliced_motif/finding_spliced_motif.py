with open("rosalind_sseq.txt", "r") as file:
	content = file.read().strip()
# skip the first empty element
raw_entries = content.split('>')[1:]
sequences = []

for entry in raw_entries:
	lines = entry.splitlines()
	sequence = "".join(lines[1:])
	sequences.append(sequence)

s = sequences[0]
t = sequences[1]

positions = []

current_s_index = 0
for base in t:
	while s[current_s_index] != base:
		current_s_index += 1
	# found the base in s, record position
	positions.append(current_s_index + 1)  # +1 for 1-based index
	current_s_index += 1
# * unpacks the list and prints separated by spaces
print(*positions)