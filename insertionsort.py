def insertionsort(A):
	for index in range(0, len(A)):
		key = A[index]
		i = index - 1
		while(i > 0 and A[i] > key):
			A[i + 1] = A[i]
			i -= 1
		A[i + 1] = key
	print(A)

A = [5, 2, 4, 6, 1, 3]
print(A)
insertionsort(A)