from Bio.Seq import Seq
# pip install biopython before

with open("rosalind_ini.txt", "r") as file:
	my_seq = Seq(file.read().strip())

# order: A, C, G, T
print(my_seq.count("A"), my_seq.count("C"), my_seq.count("G"), my_seq.count("T"))