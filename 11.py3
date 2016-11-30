s = list(open('input11.txt').readline())

def ok(s):
	ok1 = 'i' not in s and 'o' not in s and 'l' not in s and \
		any(ord(s[i]) + 2 == ord(s[i+1]) + 1 == ord(s[i+2]) for i in range(len(s)-2))
	if not ok1: return False

	a = min((i for i in range(len(s)-1) if s[i] == s[i+1]), default=-1)
	if a == -1:	return False

	b = min((i for i in range(len(s)-1) if s[i] == s[i+1] and s[i] != s[a]), default=-1)
	return b != -1


while 1:
	at = len(s)-1
	while s[at] == 'z':
		s[at] = 'a'
		at -= 1
	s[at] = chr(ord(s[at])+1)
	if ok(s):
		print(''.join(s))



