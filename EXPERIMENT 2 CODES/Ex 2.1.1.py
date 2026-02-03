# Write your code here...
a,b,c = map(float,input().split())#space separated mapinto the variable

D = (b * b) - (4 * a * c)
sqrD = D ** 0.5



if D > 0:
	root1 = (-b + sqrD)/(2*a)
	root2 = (-b - sqrD)/(2*a)
	print(f"root1 = {root1 :.2f}")
	print(f"root2 = {root2 :.2f}")

elif D == 0:
	root = -b / (2*a)
	print(f"root1 = root2 = {root:.2f}")

else:
	real_part = (-b) / (2*a)
	imaginary_part = sqrD / (2*a)

	print(f"root1 = {real_part :.2f}+{imaginary_part.imag :.2f}i")
	print(f"root2 = {real_part :.2f}-{imaginary_part.imag :.2f}i")
