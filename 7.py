import fileinput
import re
d={}
for l in fileinput.input():
	l=l.strip()
	m=re.match(r'(.*?) -> (\w+)',l).groups()
	d[m[1]]=m[0]

def mg(r,s):
	m=re.match(r+'$',s)
	if not m: return []
	return m.groups()

def r(v):
	m=mg(r'(\d+)',v)
	if m:
		return int(m[0])
	print 'r({}): {}'.format(v,d[v])
	if isinstance(d[v],int): return d[v]
	c=d[v]
	m=mg(r'(\d+)',c)
	if m:
		d[v]=int(m[0])
		return d[v]
	m=mg(r'(\w+)',c)
	if m:
		d[v]=r(m[0])
		return d[v]
	m=mg(r'NOT (\w+)',c)
	if m:
		d[v]=~r(m[0])&0xffff
		return d[v]
	m=mg(r'(\w+) AND (\w+)',c)
	if m:
		d[v]=r(m[0])&r(m[1])
		return d[v]
	m=mg(r'(\w+) OR (\w+)',c)
	if m:
		d[v]=r(m[0])|r(m[1])
		return d[v]
	m=mg(r'(\w+) LSHIFT (\w+)',c)
	if m:
		d[v]=(r(m[0])<<r(m[1]))&0xffff
		return d[v]
	m=mg(r'(\w+) RSHIFT (\w+)',c)
	if m:
		d[v]=r(m[0])>>r(m[1])
		return d[v]

print r('a')