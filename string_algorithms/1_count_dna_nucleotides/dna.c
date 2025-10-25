#include <stdio.h>

int main(void)
{
	int A = 0, C = 0, G = 0, T = 0;
	int base;
	// FILE *seq = fopen("rosalind_dna.txt", "r");
	// if (seq == NULL) return 1;

	while (base != '\n' && (base = getchar()) != EOF)
	{
		if (base == 'A') A++;
		else if (base == 'C') C++;
		else if (base == 'G') G++;
		else if (base == 'T') T++;
	}

	// fclose(seq);
	printf("%d %d %d %d\n", A, C, G, T);
	return 0;
}


// gcc dna.c -o dna
// cat rosalind_dna.txt | ./dna
// ./dna < rosalind_dna.txt
