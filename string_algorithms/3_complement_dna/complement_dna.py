'''
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc
 formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

Sample Dataset
AAAACCCGGT
Sample Output
ACCGGGTTTT
'''

import sys

file = open(sys.argv[1])
dna_s = file.read().strip()

dna_reversed = reversed(dna_s)
dna_sc = ''

complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

for base in dna_reversed:
	dna_sc += complement[base]
print(dna_sc)

# python3 complement_dna.py dna.txt