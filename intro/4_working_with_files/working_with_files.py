with open("rosalind_ini5.txt", "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    if i % 2 == 1:
        print(lines[i].strip())