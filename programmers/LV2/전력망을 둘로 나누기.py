from collections import defaultdict


def dfs(graph, start, disconnect):

    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        visited.append(now)
        for n in graph[now]:
            if n == disconnect:
                continue
            if n not in visited:
                stack.append(n)
    return len(visited)


def solution(n, wires):

    answer = 1e9

    tree = defaultdict(list)
    for s, e in wires:
        tree[s].append(e)
        tree[e].append(s)

    for s, e in wires:
        cnt = dfs(tree, s, e)
        answer = min(answer, abs(n - 2 * cnt))
    print(answer)
    return answer


solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])


def solution2(n, wires):
    answer = int(1e9)

    tree = {}

    for wire in wires:
        a, b = wire

        if a in tree:
            tree[a].append(b)
        else:
            tree[a] = [b]

        if b in tree:
            tree[b].append(a)
        else:
            tree[b] = [a]

    for wire in wires:
        power = [0, 0]
        for i, root in enumerate(wire):
            queue = [root]
            visited = [wire[i - 1]]

            while queue:
                node = queue.pop(0)
                if node in visited:
                    continue
                visited.append(node)

                for child in tree[node]:
                    if child not in visited:
                        queue.append(child)

            power[i] = len(visited)

        answer = min(answer, abs(power[0] - power[1]))

    return answer
