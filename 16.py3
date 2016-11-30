m = {
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1,
}

for line in open('input16.txt').readlines():
	line = line.strip() + ','
	buang = False
	for k, v in m.items():
		if k in line and '{}: {},'.format(k, v) not in line:
			buang = True
			break
	if not buang:
		print(line)
