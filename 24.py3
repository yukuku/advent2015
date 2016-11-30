P = sorted(map(int, open('input24.txt').readlines()), reverse=True)
N = len(P)
target = sum(P)//3

minpake = 9e9
minkal = 9e9

def coba(pake, start, jum, kal):
	global minpake, minkal

	if jum == target:
		if pake < minpake or (pake == minpake and kal < minkal):
			minpake = pake
			minkal = kal
			print(minpake, minkal)
	elif jum < target:
		for i in range(start, N):
			coba(pake+1, start+1, jum+P[i], kal*P[i])

coba(0, 0, 0, 1)
