import re
from collections import defaultdict


# preprocess to one char each
R = re.compile('e|[A-Z][a-z]*')
N = {}
def prep(s):
	res = ''
	for t in re.finditer(R, s):
		n = t.group()
		if n == 'e':
			res += n
		else:
			if n not in N:
				N[n] = chr(65+len(N))
			res += N[n]
	return res

m = {}
for line in open('input19.txt').readlines():
	line = line.strip()
	if '=>' in line:
		line = line.split()
		k = prep(line[2])
		if k in m:
			raise ValueError()
		m[k] = prep(line[0])
	elif not line:
		pass
	else:
		S = prep(line)

print(S)
for k in sorted(m.keys()):
	print(k, '=>', m[k])

while 1:
	got = False

	print('cur input: {}'.format(S))
	for k in m:
		pos = 0
		while 1:
			pos = S.find(k, pos)
			if pos >= 0:
				print('- {} at {}'.format(k, pos))
				pos += 1
			else: break


	for i in range(1, len(S)+1):
		for j in range(i-1, -1, -1):
			k = S[j:i]
			if k in m:
				S = S[:j] + m[k] + S[i:]
				got = True
				break
		if got: break
	if not got: break
print(S)

