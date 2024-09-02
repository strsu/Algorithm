N = int(input())

won_5, N = divmod(N, 5)
won_2, N = divmod(N, 2)

if N:
    for i in range(1, won_5 + 1):
        new_won_2, N = divmod(N + i * 5, 2)
        if N == 0:
            won_5 -= i
            won_2 += new_won_2
            break

if N:
    print(-1)
else:
    print(won_2 + won_5)
