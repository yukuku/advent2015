city_names = {}
d = {}

for s in open('input9.txt').readlines():
	x, y = s.split(' = ')
	y = int(y)
	a, b = x.split(' to ')
	if a not in city_names:
		city_names[a] = len(city_names)
	a = city_names[a]
	if b not in city_names:
		city_names[b] = len(city_names)
	b = city_names[b]
	d[(a, b)] = y
	d[(b, a)] = y

v = [False] * len(city_names)
mx = 0

def run(cur, dep, tot):
	global mx
	if dep == len(city_names) - 1:
		mx = max(mx, tot)
		return

	for t in range(len(city_names)):
		if not v[t]:
			v[t] = True
			run(t, dep+1, tot+d[(cur, t)])
			v[t] = False

for s in range(len(city_names)):
	v[s] = True
	run(s, 0, 0)
	v[s] = False

print(mx)
