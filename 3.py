import fileinput
d={}
p=(0,0)
d[p]=1
for l in fileinput.input():
	for c in l:
		if c=='^': p=(p[0]-1,p[1])
		if c=='v': p=(p[0]+1,p[1])
		if c=='<': p=(p[0],p[1]-1)
		if c=='>': p=(p[0],p[1]+1)
		d[p]=1

print len(d)
