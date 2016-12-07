import fileinput
r=0
for l in fileinput.input():
	l=l.strip()
	if sum(1 if c in 'aiueo' else 0 for c in l)>=3:
		if any(l[i]==l[i+1] for i in range(len(l)-1)):
			if 'ab' not in l and 'cd' not in l and 'pq' not in l and 'xy' not in l:
				r+=1
print r

