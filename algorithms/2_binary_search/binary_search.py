with open('rosalind_bins.txt', 'r') as file:
    # n and m will not be needed in Python
    n = int(file.readline().strip())
    m = int(file.readline().strip())
    A = list(map(int, file.readline().split()))
    keys = list(map(int, file.readline().split()))
results = []

for k in keys:
    low = 0
    high = len(A) - 1
    found_at = -1
    
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == k:
            found_at = mid + 1  # bc index starts with 1, not 0
            break
        elif A[mid] < k:
            low = mid + 1
        else:
            high = mid - 1

    results.append(str(found_at))

#print(" ".join(results))
with open('output.txt', 'w') as file_out:
    file_out.write(" ".join(results))