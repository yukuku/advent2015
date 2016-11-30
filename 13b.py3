p = {}
names = {}

for line in open('input13.txt').readlines():
	line = line.split()
	a = line[0]
	y = (-1 if line[2] == 'lose' else 1) * int(line[3])
	b = line[10][:-1]
	if a not in names:
		names[a] = len(names)
	a = names[a]
	if b not in names:
		names[b] = len(names)
	b = names[b]
	p[(a, b)] = y

# add myself
me = len(names)
names['myself'] = me
for i in range(len(names) - 1):
	p[(i, me)] = 0
	p[(me, i)] = 0

n = len(names)
v = [False] * n
f = [-1] * n

mx = 0

def go(cur, dep, tot):
	global mx
	f[dep] = cur
	if dep != 0:
		tot += p[(f[dep-1], cur)]
		tot += p[(cur, f[dep-1])]
	if dep == n-1:
		tot += p[(f[0], cur)]
		tot += p[(cur, f[0])]
		print(f, tot)
		mx = max(mx, tot)
		return
	for nxt in range(n):
		if not v[nxt]:
			v[nxt] = True
			go(nxt, dep+1, tot)
			v[nxt] = False

for s in range(n):
	v[s] = True
	go(s, 0, 0)
	v[s] = False

print(mx)
