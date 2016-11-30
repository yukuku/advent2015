C = list(map(int, open('input17.txt').readlines()))

res = 0
for i in range(2**len(C)):
	s = 0
	for j in range(len(C)):
		if i&(1<<j):
			s += C[j]
	if s == 150:
		res += 1
print(res)
