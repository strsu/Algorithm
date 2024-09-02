"""
H 로 시작하면 햄버거가 사람을
P 로 시작하면 사림이 햄버거를 먹자
"""

N, K = map(int, input().split())
table = list(input())

answer = 0

for i in range(N):
    if table[i] == "P":
        for j in range(1, K + 1):
            if i + j < N:
                if table[i + j] == "H":
                    table[i + j] = "-"
                    answer += 1
                    break
            else:
                break
    elif table[i] == "H":
        for j in range(1, K + 1):
            if i + j < N:
                if table[i + j] == "P":
                    table[i + j] = "-"
                    answer += 1
                    break
            else:
                break

print(answer)
