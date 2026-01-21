with open("rosalind_ini4.txt", "r") as file:
	nums = file.read().split()
	a=int(nums[0])
	b=int(nums[1])
	total_sum = 0
	for i in range(a,b+1):
		if i%2==1:
			total_sum += i
	print(total_sum)