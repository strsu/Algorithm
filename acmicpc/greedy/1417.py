N = int(input())
dasom = int(input())
candi = [int(input()) for _ in range(N - 1)]

answer = 0

while candi:
    candi.sort()
    someone = candi.pop()
    if dasom > someone:
        break
    dasom += 1
    answer += 1
    someone -= 1
    candi.append(someone)

print(answer)
