P = sorted(map(int, open('input24.txt').readlines()))
target = sum(P)//4

dp = {}
dp[0] = (0, 1)

for p in P:
	for i in range(target, -1, -1):
		if i in dp:
			dp[i+p] = (dp[i][0]+1, dp[i][1]*p) if i+p not in dp else min(dp[i+p], (dp[i][0]+1, dp[i][1]*p))
print(dp[target])

