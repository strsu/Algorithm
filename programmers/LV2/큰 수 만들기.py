from collections import deque


def solution_v1(number, k):
    number = deque(list(number))
    left = sorted(number, reverse=True)

    answer = []

    while k:
        for n in left:
            idx = number.index(n)
            if idx <= k:
                for _ in range(idx):
                    number.popleft()
                    k -= 1
                answer.append(number.popleft())
                left = sorted(number, reverse=True)
                break

    answer += number

    return "".join(answer)


def solution_v2(number, k):
    number = deque(list(number))

    for i in range(len(number) - k):
        for j in range(i + 1, i + k + 1):
            if number[i] < number[j]:
                number = number[:i] + number[i + 1 :]
                k -= 1
                break

    return "".join(number)


def solution(number, k):
    number = deque(list(number))

    while k:
        

    return "".join(number)


answer = solution("4177252841", 4)

print(answer)
