#include <stdio.h>

int main(void)
{
	int base;
	char rna_base;

	FILE *dna = fopen("rosalind_rna.txt", "r");
	if (dna == NULL)
		return 1;

	while ((base = fgetc(dna)) != EOF)
	{
		char rna_base = (char)base;
		if (rna_base == 'T')
			putchar('U');
		else
			putchar(rna_base);
	}

	fclose(dna);
	return 0;
}