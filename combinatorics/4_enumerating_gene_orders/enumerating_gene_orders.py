import itertools

with open('rosalind_perms.txt', 'r') as file:
    n = int(file.read().strip())

nums = range(1, n + 1)
perms = list(itertools.permutations(nums))

print(len(perms))
for p in perms:
    print(*p)