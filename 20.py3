from itertools import count

z = int(open('input20.txt').readline())//10

MAX = 1000000
k = [0]*MAX
for j in range(1, MAX):
	p = j
	while p < MAX:
		k[p] += j
		p += j

for i in range(MAX):
	if k[i] >= z:
		print(i)
		break
