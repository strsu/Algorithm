N, D = map(int, input().split())

selected = []
distance = []

for _ in range(N):
    s, e, d = map(int, input().split())
    if e > D:
        continue
    if d >= e - s:
        continue
    distance.append((s, e, d, round(d / (e - s), 3)))

distance.sort(key=lambda x: x[3])

while distance:
    s, e, d, _ = distance.pop(0)

    valid = True
    for select in selected:
        if s == select[0] and e == select[1]:
            valid = False
            break
        if s < select[0] < e or s < select[1] < e:
            valid = False
            break

    if valid:
        selected.append((s, e, d))

answer = 0
now = 0

for select in selected:
    s, e, d = select

    answer += s - now + d
    now = e

answer += D - now

print(answer)
