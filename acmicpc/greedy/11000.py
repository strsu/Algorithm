N = int(input())

coun = sorted(
    [list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0])
)

room = 0
N -= 1
idx = 0
now = coun.pop(0)

while coun:
    if coun[idx % N][0] >= now[1]:
        now = coun.pop(idx % N)
        N -= 1
    else:
        now = coun.pop(idx % N)
        room += 1
    idx += 1

print(room)
