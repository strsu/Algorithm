# N, H = map(int, input().split())
# building = list(map(int, input().split()))

# answer = 0

# for i in range(len(building)):
#     highest = 0
#     cnt = 0
#     for j in range(i + 1):
#         if building[i - j] >= H:
#             break

#         if building[i - j] > highest:
#             cnt += 1
#             highest = building[i - j]
#     print(i, cnt)
#     answer = max(answer, cnt)

# print(answer)

N, H = map(int, input().split())
building = list(map(int, input().split()))

answer = [0] * len(building)

for i in range(len(building)):
    if building[i] < H:
        for j in range(i - 1, -1, -1):
            if building[j] > building[i]:
                answer[i] = answer[j] + 1
                break

print(max(answer))
