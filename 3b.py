import fileinput
d={}
p=(0,0)
d[p]=1
p1=p
p2=p
for l in fileinput.input():
	k=0
	for c in l:
		if k==0: p=p1
		else: p=p2
		if c=='^': p=(p[0]-1,p[1])
		if c=='v': p=(p[0]+1,p[1])
		if c=='<': p=(p[0],p[1]-1)
		if c=='>': p=(p[0],p[1]+1)
		d[p]=1
		if k==0: p1=p
		else: p2=p
		k=1-k

print len(d)
