with open("rosalind_ini3.txt", "r") as file:
    lines = file.readlines()
#print(lines)

s = lines[0].strip()

nums = lines[1].strip().split()
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
d = int(nums[3])

print(s[a:b+1] + " " + s[c:d+1])