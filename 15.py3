A = []

for line in open('input15.txt').readlines():
	line = line.replace(',', ' ').split()
	x = [int(line[2]), int(line[4]), int(line[6]), int(line[8])]
	A.append(x)

mx = 0
for a in range(100+1):
	for b in range(100-a+1):
		for c in range(100-a-b+1):
			d = 100-a-b-c
			s = 1
			for k in range(4):
				t = a*A[0][k] + b*A[1][k] + c*A[2][k] + d*A[3][k]
				if t <= 0:
					s = 0
					break
				s *= t
			mx = max(mx, s)
print(mx)

