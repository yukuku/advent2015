line = open('input25.txt').readline().replace(',', ' ').replace('.', ' ').split()
R = int(line[15])
C = int(line[17])

r = 1
c = 1
n = 20151125

while 1:
	n = (n*252533)%33554393
	r -= 1
	c += 1

	if r == 0:
		r = c
		c = 1

	if r == R and c == C:
		print(n)
		break