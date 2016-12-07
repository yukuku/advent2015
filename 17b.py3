C = list(map(int, open('input17.txt').readlines()))

mi = 9e9
res = 0
for i in range(2**len(C)):
	s = 0
	c = 0
	for j in range(len(C)):
		if i&(1<<j):
			s += C[j]
			c += 1
	if s == 150:
		res += 1
		mi = min(mi, c)

res = 0
for i in range(2**len(C)):
	s = 0
	c = 0
	for j in range(len(C)):
		if i&(1<<j):
			s += C[j]
			c += 1
	if s == 150 and c == mi:
		res += 1

print(res)
