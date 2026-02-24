# Type Content here...
x,y,z = input().split()
combi = [x,y,z]

for i in range(3):
	for j in range(3):
		for k in range(3):
			if i!=j and i!=k and j!=k:
				print(combi[i]+combi[j]+combi[k])
