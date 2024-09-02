N = int(input())
values = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    v = values[i]
    for j in range(i):
        if values[i] > values[j]:
            v += values[j]
    dp[i] = v

print(dp)
print(max(dp))
