def solution(edges):
    in_edge = set()
    graph = {}

    for vs in edges:
        s, e = vs
        if s not in graph:
            graph[s] = []

        # 들어오는 간선이 없는 노드를 찾기
        in_edge.add(e)

        graph[s].append(e)

    # 추가된 정점 찾기
    added_node = list(graph.keys() - in_edge)
    for ad in added_node:
        if len(graph[ad]) > 1:
            added_node = ad
            break

    answer = [added_node, 0, 0, 0]

    for v in graph.pop(added_node):
        if v not in graph:
            graph[v] = []

    while graph:
        start = list(graph.keys())[0]

        v = set([start])
        e = graph.pop(start)
        idx = 0

        while idx < len(e):
            next = e[idx]

            v.add(next)
            e += graph.pop(next, [])

            idx += 1

        if len(v) == len(e):
            answer[1] += 1
        elif len(v) == len(e) + 1:
            answer[2] += 1
        elif len(v) == len(e) - 1:
            answer[3] += 1

    return answer


edges = [
    [1, 2],
    [3, 4],
    [5, 1],
    [5, 3],
    [6, 7],
    [7, 8],
    [8, 7],
    [7, 6],
    [5, 6],
]

solution(edges)
