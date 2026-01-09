with open('rosalind_fibd.txt', 'r') as file:
    data = file.readline().split()
    n = int(data[0])  # number of months of observation
    m = int(data[1])  # number of months a rabbit lives

ages = [0] * m # list of rabbits by age: 0 newborn, m-1 oldest (bc in month m - rabbit already dies)
ages[0] = 1 # in the beginning we have 1 pair

for i in range(n - 1):
    # slicing newborns (ages 1 and older)
    new_borns = sum(ages[1:])
    # new list: newborns added to the beginning of the list and ages[:-1] slicing all except the oldest generation (dead)
    ages = [new_borns] + ages[:-1]
print(sum(ages))