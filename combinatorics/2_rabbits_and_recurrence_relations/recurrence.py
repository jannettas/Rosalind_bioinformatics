with open('rosalind_fib.txt', 'r') as file:
    line = file.readline()
    data = line.split()  
    n = int(data[0]) 
    k = int(data[1])

f_n2 = 1
f_n1 = 1

if n < 3:
    result = 1
else:
    for i in range(3, n + 1):
        f_current = f_n1 + (k * f_n2)
        f_n2 = f_n1
        f_n1 = f_current  
    result = f_n1
print(result)