N = int(input())
M = int(input())

graph = [[-1] * N for _ in range(N)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s - 1][s - 1] = 0
    graph[e - 1][e - 1] = 0
    graph[s - 1][e - 1] = t

for g in graph:
    print(g)

s, e = map(int, input().split())

visited = [False] * N
visited[s - 1] = True
dist = graph[s - 1]


def get_next(dist, visited):
    val = 10000000
    idx = 1
    for i, v in enumerate(visited):
        if not v:
            if dist[i] < val:
                val = dist[i]
                idx = i

    return idx


while False in visited:
    next = get_next(dist, visited)
    visited[next] = True
    for i, v in enumerate(graph[next]):
        if v != -1:
            dist[i] = min(dist[i], dist[next] + v)

print(dist[e - 1])
