import re
from collections import defaultdict

m = defaultdict(list)

for line in open('input19.txt').readlines():
	line = line.strip()
	if '=>' in line:
		line = line.split()
		m[line[0]].append(line[2])
	elif not line:
		pass
	else:
		s = line

r = re.compile('[A-Z][a-z]*')
Z = set()
for t in re.finditer(r, s):
	u = t.group()
	for v in m[u]:
		z = s[:t.start()] + v + s[t.end():]
		Z.add(z)
print(len(Z))
