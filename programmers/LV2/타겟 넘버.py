def solution(numbers, target):

    num = numbers.pop(0)
    cur_numbers = [num, -num]

    while numbers:
        next_numbers = []
        num = numbers.pop(0)
        for cur in cur_numbers:
            next_numbers.append(cur + num)
            next_numbers.append(cur - num)
        cur_numbers = next_numbers

    return cur_numbers.count(target)


print(solution([4, 1, 2, 1], 4))

# def solution(numbers, target):
#     answer = 0
#     l = len(numbers)

#     def DFS(cur_idx, sum):
#         nonlocal answer
#         if cur_idx == l:
#             if sum == target:
#                 answer += 1
#             return True
#         else:
#             DFS(cur_idx+1, sum+numbers[cur_idx])
#             DFS(cur_idx+1, sum-numbers[cur_idx])

#     DFS(0,0)

#     return answer
