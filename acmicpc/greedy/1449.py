N, L = map(int, input().split())
arr = sorted(list(map(int, input().split())))

tape_cnt = 0

while arr:
    s_idx = 0
    e_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[s_idx] - 0.5 + L:
            e_idx = i
        else:
            break
    tape_cnt += 1
    arr = arr[e_idx + 1 :]

print(tape_cnt)
