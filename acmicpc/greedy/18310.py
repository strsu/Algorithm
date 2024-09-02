import random

N = int(input())
# house = sorted(list(map(int, input().split())))
house = sorted([random.randint(1, 200000) for _ in range(N)])

mid = N // 2
valid_left = True
valid_right = True

min_left = -1
min_right = -1

answer = house[mid]

for i in range(N):
    if valid_left:
        now_dist = 0
        for nh in house:
            now_dist += abs(house[mid - i] - nh)
        if min_left == -1:
            answer = house[mid - i]
            min_left = now_dist
        else:
            if now_dist <= min_left:
                answer = house[mid - i]
                min_left = now_dist
            elif now_dist > min_left:
                valid_left = False
    if valid_right:
        now_dist = 0
        for nh in house:
            now_dist += abs(house[mid - i] - nh)
        if min_right == -1:
            answer = house[mid - i]
            min_right = now_dist
        else:
            if now_dist < min_right:
                answer = house[mid - i]
                min_right = now_dist
            elif now_dist > min_right:
                valid_right = False

    if not valid_left and not valid_right:
        break


print(answer)

print(house[(N - 1) // 2])
