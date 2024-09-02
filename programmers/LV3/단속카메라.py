def solution(routes):

    print(sorted(routes, key=lambda x: x[1]))

    answer = 0

    routes.sort()

    while routes:
        s, e = routes.pop(0)

        idx = 0
        while idx < len(routes):
            ns, ne = routes[idx]
            if s <= ns <= e:
                if ns > s:
                    s = ns
                if ne < e:
                    e = ne
            else:
                break
            idx += 1

        answer += 1
        routes = routes[idx:]

    return answer


solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3], [1, 6], [2, 7]])
solution([[-20, -15], [-18, -17], [-14, -5], [-5, -3], [1, 20], [10, 12], [15, 17]])
