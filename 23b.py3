prog = []
pc = 0

for line in open('input23.txt').readlines():
	line = line.strip().replace(',', ' ').split()
	if line[0] in ['hlf', 'tpl', 'inc']:
		prog.append([line[0], line[1]])
	elif line[0] in ['jmp']:
		prog.append([line[0], int(line[1])])
	else:
		prog.append([line[0], line[1], int(line[2])])

a = 1
b = 0

while 1:
	if pc < 0 or pc >= len(prog): break
	s = prog[pc]

	print(pc, s, a, b)

	if s[0] == 'hlf':
		if s[1]=='a': a //= 2
		if s[1]=='b': b //= 2
		pc += 1
	elif s[0] == 'tpl':
		if s[1]=='a': a *= 3
		if s[1]=='b': b *= 3
		pc += 1
	elif s[0] == 'inc':
		if s[1]=='a': a += 1
		if s[1]=='b': b += 1
		pc += 1
	elif s[0] == 'jmp':
		pc += s[1]
	elif s[0] == 'jie':
		if s[1]=='a': k = a
		if s[1]=='b': k = b
		if k%2 == 0:
			pc += s[2]
		else:
			pc += 1
	elif s[0] == 'jio':
		if s[1]=='a': k = a
		if s[1]=='b': k = b
		if k == 1:
			pc += s[2]
		else:
			pc += 1

print(a, b, pc)

