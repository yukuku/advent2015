mx = 0

for line in open('input14.txt').readlines():
	line = line.split()
	v = int(line[3])
	t = int(line[6])
	r = int(line[13])

	f = 2503 // (t+r)
	mx = max(mx, v*t*f + v*min(2503 % (t+r), t))

print(mx)

