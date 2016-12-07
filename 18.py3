m = []

for line in open('input18.txt').readlines():
	m.append(list(line.strip()))

def step(m):
	n = [[0]*len(m[0]) for _ in range(len(m))]
	R = len(m)
	C = len(m[0])
	for r in range(len(m)):
		for c in range(len(m[r])):
			y = 0
			if r>0:
				if m[r-1][c] == '#': y += 1
				if c>0:
					if m[r-1][c-1] == '#': y += 1
				if c<C-1:
					if m[r-1][c+1] == '#': y += 1
			if r<R-1:
				if m[r+1][c] == '#': y += 1
				if c>0:
					if m[r+1][c-1] == '#': y += 1
				if c<C-1:
					if m[r+1][c+1] == '#': y += 1
			if c>0:
				if m[r][c-1] == '#': y += 1
			if c<C-1:
				if m[r][c+1] == '#': y += 1

			if (m[r][c]=='#' and (y==2 or y==3)) or (m[r][c]=='.' and y==3):
				n[r][c] = '#'
			else:
				n[r][c] = '.'
	return n

for _ in range(100):
	m = step(m)

print(sum(sum(m[r][c]=='#' for c in range(len(m[0]))) for r in range(len(m))))
