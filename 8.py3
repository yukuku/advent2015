a = 0
b = 0

for s in open('input8.txt').readlines():
	a += len(s)
	s = s[1:-1]
	i = 0
	while 1:
		if i >= len(s): break
		c = s[i]
		if c == '\\':
			i += 1
			if s[i] == 'x':
				i += 2
		i += 1
		b += 1
		
print(a - b)
