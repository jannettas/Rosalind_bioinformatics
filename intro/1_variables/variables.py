with open("rosalind_ini2.txt", "r") as file:
    # Code to read the data goes here
	line = file.readline().strip()
	parts = line.split()
	a = int(parts[0])
	b = int(parts[1])
	result = (a**2 + b**2)
	print(result)