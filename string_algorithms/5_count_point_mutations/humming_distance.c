#include <stdio.h>

int main()
{
	char both_seq_file[2005];
	char base;
	int both_seq_len = 0;
	int count = 0;
	int half = 0;

	FILE *f = fopen("rosalind_hamm.txt", "r");
	if (f == NULL)
	{
		printf("Error opening file.\n");
		return 1;
	}

	while ((base = fgetc(f)) != EOF)
	{
		if (base == 'A' || base == 'C' || base == 'G' || base == 'T')
		{
			both_seq_file[both_seq_len] = base;
			both_seq_len++;
		}
	}

	half = both_seq_len / 2;
	for (int i = 0; i < half; i++)
	{
		if (both_seq_file[i] != both_seq_file[i + half])
			count++;
	}
	printf("%d\n", count);
	fclose(f);
	return 0;
}