b = 0

for s in open('input8.txt').readlines():
	b += 2
	for c in s:
		if c == '\\' or c == '"': b += 1
		
print(b)
