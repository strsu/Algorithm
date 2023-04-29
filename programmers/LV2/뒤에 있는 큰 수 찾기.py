from collections import deque


def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [numbers.pop()]

    for i, n in enumerate(numbers[::-1]):
        while stack:
            root = stack.pop()
            if root > n:
                answer[-2 - i] = root
                stack.append(root)
                stack.append(n)
                break
        if not stack:
            stack.append(n)
    return answer
