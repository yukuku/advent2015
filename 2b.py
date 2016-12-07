import fileinput
t = 0
for l in fileinput.input():
	s = [int(x) for x in l.strip().split('x')]
	st = sorted(s)[0:2]
	b=2*(st[0]+st[1])
	b+=s[0]*s[1]*s[2]
	t+=b
	print b
print t
