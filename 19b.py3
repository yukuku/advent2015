import re
from collections import defaultdict

m = {}
maxlen = 0
for line in open('input19.txt').readlines():
	line = line.strip()
	if '=>' in line:
		line = line.split()
		maxlen = max(maxlen, len(line[2]))
		m[line[2]] = line[0]
	elif not line:
		pass
	else:
		S = line

Z = set()
def dfs_expand(s, d):
	print(s, d)

	if s == 'e':
		print(d)
		return

	for i in range(len(s)):
		if 'A'<=s[i]<='Z':
			for j in range(min(i+maxlen, len(s))-1, i, -1):
				k = s[i:j]
				if k in m:
					v = m[k]
					z = s[:i] + v + s[j:]
					if z not in Z:
						Z.add(z)
						dfs_expand(z, d+1)

dfs_expand(S, 0)
