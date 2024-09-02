def solution(sequence):

    dp_1 = [0] * len(sequence)
    dp_2 = [0] * len(sequence)
    sign_1 = 1
    sign_2 = -1

    dp_1[0] = sequence[0] * sign_1
    dp_2[0] = sequence[0] * sign_2

    for i in range(1, len(sequence)):
        sign_1 *= -1
        sign_2 *= -1
        dp_1[i] = max(dp_1[i - 1] + sequence[i] * sign_1, sequence[i] * sign_1)
        dp_2[i] = max(dp_2[i - 1] + sequence[i] * sign_2, sequence[i] * sign_2)

    return max(dp_1 + dp_2)


answer = solution([2, 3, -6, 1, 3, -1, 2, 4])
print(answer)
