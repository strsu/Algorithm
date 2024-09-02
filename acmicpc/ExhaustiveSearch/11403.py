N = int(input())

graph = {i: set() for i in range(N)}

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            graph[i].add(j)

for i in range(N):
    g = [0] * N
    v = list(graph[i])
    visited = []
    while v:
        j = v.pop()
        visited.append(j)
        g[j] = 1
        for m in graph[j]:
            if m not in visited:
                v.append(m)
    print(" ".join(map(str, g)))
