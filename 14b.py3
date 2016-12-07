from collections import namedtuple

R = namedtuple('R', 'v t r')

rs = []
ps = {}
ws = {}

for line in open('input14.txt').readlines():
	line = line.split()
	v = int(line[3])
	t = int(line[6])
	r = int(line[13])

	rs.append(R(v,t,r))

for i in range(2503):
	for r in rs:
		f = i % (r.t+r.r)
		if f < r.t:
			ps[r] = ps.get(r, 0) + r.v
	win = max(ps[r] for r in rs)
	for r in rs:
		if ps[r] == win:
			ws[r] = ws.get(r, 0) + 1

print(max(ws.get(r, 0) for r in rs))
