"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u 
is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset
GATGGAACTTGACTACGTAAATT

Sample Output
GAUGGAACUUGACUACGUAAAUU
"""

dna = input("Enter DNA sequence: ").upper()

# replace Tymine with Uracil
rna = dna.replace('T', 'U')

# rna = ''
# for base in dna:
# 	if base == 'T':
# 		rna += 'U'
# 	else:
# 		rna += base

print(rna)