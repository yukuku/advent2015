s = open('input10.txt').readline()

def proc(s):
	lc = None
	ln = 0
	res = ''
	for c in s:
		if c != lc:
			if lc is not None:
				res += str(ln) + str(lc)
			lc = c
			ln = 1
		else:
			ln += 1
	if lc is not None:
		res += str(ln) + str(lc)
	return res


for _ in range(50):
	s = proc(s)
print(len(s))
