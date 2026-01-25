import itertools

with open("rosalind_lexf.txt", "r") as file:
    # first line split it into a list of chars
    alphabet = file.readline().split()
    
    # second line - length n
    n = int(file.readline().strip())

# print(f"Alphabet: {alphabet}")
# print(f"Length n: {n}")

# generate all possible strings of length n
results = itertools.product(alphabet, repeat=n)

# join the tuples into strings and print them
for p in results:
    print("".join(p))
    
# # solution with recursion - also works
# def generate_strings(alphabet, n, current_string=""):
#     # if the string is the length we want, print it
#     if len(current_string) == n:
#         print(current_string)
#         return

#     # recursion: try adding every letter from the alphabet
#     for char in alphabet:
#         generate_strings(alphabet, n, current_string + char)

# generate_strings(alphabet, n)