with open('rosalind_tran.txt', 'r') as file:
    content = file.read().strip()
# skip the first empty element
raw_entries = content.split('>')[1:]

s1 = "".join(raw_entries[0].splitlines()[1:])
s2 = "".join(raw_entries[1].splitlines()[1:])

transitions = 0
transversions = 0

purines = {'A', 'G'}
pyrimidines = {'C', 'T'}

for n1, n2 in zip(s1, s2):
    if n1 != n2:
        if (n1 in purines and n2 in purines) or (n1 in pyrimidines and n2 in pyrimidines):
            transitions += 1
        else:
            transversions += 1
print(transitions / transversions)