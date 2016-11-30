from itertools import count

z = int(open('input20.txt').readline())

MAX = 10000000
k = [0]*MAX
for j in range(1, MAX//11):
	u = 11*j
	p = j
	for _ in range(50):
		if p >= MAX: break
		k[p] += u
		p += j

for i in range(MAX):
	if k[i] >= z:
		print(i)
		break
