N = int(input())

coun = sorted(
    [list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0])
)

available = [coun.pop(0)]

for c in coun:
    if available[-1][1] <= c[0]:
        available.append(c)

print(len(available))
