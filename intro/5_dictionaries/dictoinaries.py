with open("rosalind_ini6.txt", "r") as file:
	s = file.read()
dict = {}
for word in s.split():
	if word in dict:
		dict[word] = dict[word] + 1
	else:
		dict[word] = 1
#print(dict)
for key, value in dict.items():
	print(key, value)