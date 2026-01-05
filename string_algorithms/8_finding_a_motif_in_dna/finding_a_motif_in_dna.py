with open('rosalind_subs.txt', 'r') as f:

    content = f.read().split()
    s = content[0]
    t = content[1]

for i in range(len(s) - len(t) + 1):
    if s[i : i + len(t)] == t:
        print(i + 1, end=' ')