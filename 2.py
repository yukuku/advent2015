import fileinput
t = 0
for l in fileinput.input():
	s = [int(x) for x in l.strip().split('x')]
	b = 2*(s[0]*s[1]+s[1]*s[2]+s[2]*s[0])
	st = sorted(s)[0:2]
	b+=st[0]*st[1]
	t+=b
	print b
print t
