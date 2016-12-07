import json

root = json.load(open('input12.txt'))

def s(n):
	res = 0
	if isinstance(n, dict):
		if not any(v == 'red' for v in n.values()):
			for v in n.values():
				res += s(v)
	elif isinstance(n, list):
		for v in n:
			res += s(v)
	elif isinstance(n, int):
		res += n
	return res

print(s(root))
