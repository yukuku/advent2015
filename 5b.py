import fileinput
r=0
for l in fileinput.input():
	l=l.strip()
	if any(l[i]==l[i+2] for i in range(len(l)-2)):
		if any(l[i:i+2]==l[j:j+2] for i in range(len(l)-3) for j in range(i+2,len(l)-1)):
			r+=1
print r

