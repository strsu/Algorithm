T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    P = sorted(map(int, input().split()))
    answer = 0
    while M > 1:
        answer += P.pop()
        M -= 1

    m = len(P) // 2
    if len(P) % 2 == 0:
        answer += (P[m - 1] + P[m]) / 2
    else:
        answer += P[m]

    print(f"Case #{_+1}: {answer}")
