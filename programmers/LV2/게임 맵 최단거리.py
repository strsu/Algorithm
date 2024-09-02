def dfs(graph, start, end, visited, depth):

    x, y = start
    if start == end:
        return depth

    n, m = end
    min_depth = 1e9

    for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1]):
        if 0 <= x + i <= n and 0 <= y + j <= m:
            if graph[x + i][y + j]:
                if not visited[x + i][y + j]:
                    visited[x + i][y + j] = True
                    new_depth = dfs(graph, (x + i, y + j), end, visited, depth + 1)
                    min_depth = min(min_depth, new_depth)
                    visited[x + i][y + j] = False

    return min_depth


def solution(maps):

    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]

    answer = dfs(maps, (0, 0), (n - 1, m - 1), visited, 1)

    if answer == 1e9:
        return -1

    return answer


solution(
    [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 0, 1],
    ]
)

from collections import deque


def solution2(maps):
    answer = int(1e9)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    m, n = len(maps), len(maps[0])

    queue = deque([(0, 0)])
    visited = []
    while queue:
        x, y = queue.popleft()

        if (x, y) == (m - 1, n - 1):
            return maps[x][y]
        visited.append((x, y))

        for _dx, _dy in zip(dx, dy):
            if 0 <= x + _dx < m and 0 <= y + _dy < n:
                if (x + _dx, y + _dy) == (m - 1, n - 1):
                    return maps[x][y] + 1
                if maps[x + _dx][y + _dy] != 1:
                    continue
                if maps[x + _dx][y + _dy] != 0:
                    maps[x + _dx][y + _dy] = maps[x][y] + 1
                    queue.append((x + _dx, y + _dy))

    return -1
