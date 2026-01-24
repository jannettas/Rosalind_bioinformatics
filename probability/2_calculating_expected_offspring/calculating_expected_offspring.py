with open("rosalind_iev.txt", "r") as file:
	line = file.readline()
	population = list(map(int, line.split()))
	probabilities = [1, 1, 1, 0.75, 0.5, 0]
	result = 0
	for i in range(len(population)):
		result = result + (population[i] * 2 * probabilities[i])
	print(result)

# Dominant phenotype probabilities (A_):
# AA-AA, AA-Aa, AA-aa -> 1.0 (100%), even AA-aa makes all Aa (dominant)
# Aa-Aa -> 0.75 (75%) -> 3:1 ratio: AA, 2xAa (3 Dominant) vs aa (1 Recessive) = 3/4 = 0.75
# Aa-aa -> 0.5 (50%) -> half dominant, half recessive
# aa-aa -> 0 -> only recessive kids