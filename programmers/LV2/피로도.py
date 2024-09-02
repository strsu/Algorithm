def dfs(dungeons, pirodo, visited, depth):
    max_depth = depth
    for i, d in enumerate(dungeons):
        if not visited[i]:
            if pirodo >= d[0]:
                visited[i] = True
                new_depth = dfs(dungeons, pirodo - d[1], visited, depth + 1)
                max_depth = max(max_depth, new_depth)
                visited[i] = False

    return max_depth


def solution(k, dungeons):
    visited = [False] * len(dungeons)

    answer = dfs(dungeons, k, visited, 0)
    return answer


solution(80, [[80, 20], [50, 40], [30, 10]])
