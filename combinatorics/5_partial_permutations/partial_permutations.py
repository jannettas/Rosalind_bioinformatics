with open("rosalind_pper.txt", "r") as file:
    parts = file.readline().strip().split()
    n = int(parts[0])
    k = int(parts[1])

permutations = 1
for i in range(k):
    permutations *= n
    n -= 1
print(permutations % 1000000)
