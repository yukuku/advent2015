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
	line = line.strip().replace(':', ' ').replace(',', ' ').split()
	p = {
		line[2]: int(line[3]),
		line[4]: int(line[5]),
		line[6]: int(line[7]),
	}

	fail = False
	for k, v in p.items():
		gt = k in ['cats', 'trees']
		lt = k in ['pomeranians', 'goldfish']

		if not gt and not lt:
			if m[k] != v:
				fail = True
		if gt:
			if m[k] >= v:
				fail = True
		if lt:
			if m[k] <= v:
				fail = True
	
	if not fail:
		print(line)
