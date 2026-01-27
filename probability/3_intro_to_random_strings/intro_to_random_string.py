import math

with open("rosalind_prob.txt", "r") as file:
    lines = file.readlines()
    s = lines[0].strip()  # DNA string
    # second line - convert string of numbers into a list of floats
    A = list(map(float, lines[1].split()))

# print(f"String: {s}")
# print(f"GC contents array: {A}")

B = []
for x in A:
    # those probs are given
    prob_gc = x / 2
    prob_at = (1 - x) / 2
    
    # sum of logarithms for string s 
    total_log = 0
    for char in s:
        if char in 'GC':
            total_log += math.log10(prob_gc)
        else:
            total_log += math.log10(prob_at)
    
    B.append(f"{total_log:.3f}")
print(" ".join(B))