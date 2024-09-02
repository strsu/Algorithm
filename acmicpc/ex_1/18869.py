from collections import Counter

우주, 행성 = map(int, input().split())

## 멀티버스 쌍 찾기
멀티버스 = [list(map(int, input().split())) for _ in range(우주)]
이어진멀티버스 = []
for 행성들 in 멀티버스:
    행성연결 = ""
    for i in range(len(행성들) - 1):
        for j in range(i + 1, len(행성들)):
            if 행성들[i] < 행성들[j]:
                행성연결 += "0"
            elif 행성들[i] == 행성들[j]:
                행성연결 += "1"
            else:
                행성연결 += "2"
    이어진멀티버스.append(행성연결)

## 구성이 같은 행성 찾기
같은행성 = {}
for i in range(len(멀티버스) - 1):
    for j in range(i + 1, len(멀티버스)):
        if set(멀티버스[i]) == set(멀티버스[j]):
            if i not in 같은행성:
                같은행성[i] = []
            같은행성[i].append(j)

이어진멀티버스개수 = Counter(이어진멀티버스)

## 초기 정답
정답 = 0
for 키, 값 in Counter(이어진멀티버스개수).items():
    정답 += 값 - 1

## 구성이 같은 행성 제거
for 키, 값들 in 같은행성.items():
    for 값 in 값들:
        if 이어진멀티버스개수[이어진멀티버스[키]] > 1 and 이어진멀티버스개수[이어진멀티버스[값]] > 1:
            정답 -= 1
print(정답)

# 6 3
# 20 10 30 ##
# 10 20 60
# 80 25 79
# 30 50 80
# 80 25 81
# 10 20 30 ##
