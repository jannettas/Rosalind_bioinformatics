with open("rosalind_ins.txt", "r") as file:
    n = int(file.readline().strip())
    a = list(map(int, file.readline().split()))
    
swaps = 0
for i in range(1, n):
    j = i
    while j > 0 and a[j] < a[j - 1]:
        temp = a[j]
        a[j] = a[j - 1]
        a[j - 1] = temp
        swaps += 1
        j -= 1
print(swaps)