str = ""
s = input()
for i in s:
	if i.isalnum() or i.isspace():
		str = str + i
print(str)
