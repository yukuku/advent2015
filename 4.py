import sys
import md5

a=sys.stdin.read()
print a
for i in range(1, 100000000):
	b=a+str(i)
	m=md5.new()
	m.update(b)
	h=m.hexdigest()
	if h.startswith('00000'):
		print b
		break
