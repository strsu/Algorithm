N, W = map(int, input().split())

V = []
for _ in range(N):
    V.append(tuple(map(int, input().split())))

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    w, k = V[i]
    for j in range(W + 1):
        if w > j:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w] + k)

print(dp[-1][-1])
