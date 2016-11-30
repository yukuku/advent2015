import math

Z = open('input21.txt').readlines()
ehp = int(Z[0].split()[2])
eatk = int(Z[1].split()[1])
edef = int(Z[2].split()[1])

print(ehp, eatk, edef)

weps = {
   8 :    4  ,     
  10     :5  ,     
  25    : 6  ,     
  40    : 7  ,     
  74   :  8  ,
  }
arms = {
0:0,
   13 :      1,
 31   :    2,
53    :   3,
75    :   4,
102   :    5,
}
accs = {
0: (0, 0),
  25:(1, 0),
  50:(2, 0),
 100:(3, 0),
  20:(0, 1),
  40:(0, 2),
  80:(0, 3),
}

maxgold = 0
for wk, wv in weps.items():
	for ak, av in arms.items():
		for c1k, c1v in accs.items():
			for c2k, c2v in accs.items():
				if c1k == c2k: continue
				patk = wv + c1v[0] + c2v[0]
				pdef = av + c1v[1] + c2v[1]
				gold = wk + ak + c1k + c2k

				edmg = max(1, eatk-pdef)
				eturns = int(math.ceil(100/edmg))

				pdmg = max(1, patk-edef)
				pturns = int(math.ceil(ehp/pdmg))

				if pturns>eturns:
					if gold > maxgold:
						print(gold, '|', wk, ak, c1k, c2k, '|', edmg, eturns, pdmg, pturns)
						maxgold = gold

print(maxgold)

