x = int(input("dimension: "))

print("first matrix:")
M = []
for i in range(x):
	row = list(map(int, input().split()))
	M.append(row)

print("second matrix:")
N = []
for i in range(x):
	row = list(map(int, input().split()))
	N.append(row)

L =[]
for i in range(x):
	L.append([0]*x)
	
for i in range(x):
	for j in range(x):
		for k in range(x):
			L[i][j]+=M[i][k]*N[k][j]

print("Resultant Matrix:")
for i in range(x):
	print(*L[i])
