# Type Content here...
begin = int(input())
end = int(input())
found = False
for num in range(begin,end+1):
	if num > 1:
		flag = True
		for i in range(2,num):
			if num % i == 0:
				flag = False
				break
		if flag:
			print(num)
			found = True

if not found:
	print("No primes")
