with open("rosalind_lexv.txt", "r") as infile, open("output.txt", "w") as outfile:
	alphabet = infile.readline().split()
	n = int(infile.readline().strip())
    # Initialize the stack with alphabet symbols in reverse order (LIFO - first symbol of the alphabet is popped first)
	stack = alphabet[::-1]
	while stack:
		current = stack.pop()
		outfile.write(current + "\n")
		print(current)
		if len(current) < n:
			for char in reversed(alphabet):
				stack.append(current + char)

# # solution with recursion
# res = []
# def solve(current_s):
#     if len(current_s) > 0:
#         res.append(current_s)
#     if len(current_s) == n:
#         return
#     for char in alphabet:
#         solve(current_s + char)
# solve("")
# for s in res:
#     print(s)