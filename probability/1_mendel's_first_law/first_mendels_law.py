with open("rosalind_iprb.txt", "r") as file:
    line = file.readline()
    k, m, n = map(int, line.split())
# print(k, m, n)

total = k + m + n
total_combos = total * (total - 1)

# mm -> aa (prob 1/4)
prob_rec_1 = (m * (m - 1)) * 0.25

# nn -> aa (prob 1)
prob_rec_2 = (n * (n - 1)) * 1.0

# mn or nm -> aa (prob 1/2)
prob_rec_3 = (2 * m * n) * 0.5

# prob recessive (aa)
prob_recessive = (prob_rec_1 + prob_rec_2 + prob_rec_3) / total_combos

# prob dominant (AA or Aa)
prob_dominant = 1 - prob_recessive

print(f"{prob_dominant:.5f}")