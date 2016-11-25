import fileinput
import re
d=[[0 for _ in range(1000)] for _ in range(1000)]
for l in fileinput.input():
	l=l.strip()
	m=re.match(r'(.*?) (\d+),(\d+) through (\d+),(\d+)',l).groups()
	fx=int(m[1])
	fy=int(m[2])
	tx=int(m[3])
	ty=int(m[4])
	if m[0]=='turn on':
		for x in range(fx,tx+1):
			for y in range(fy,ty+1): d[x][y]=1
	if m[0]=='turn off':
		for x in range(fx,tx+1):
			for y in range(fy,ty+1): d[x][y]=0
	if m[0]=='toggle':
		for x in range(fx,tx+1):
			for y in range(fy,ty+1): d[x][y]=1-d[x][y]

print sum(sum(c for c in r) for r in d)

