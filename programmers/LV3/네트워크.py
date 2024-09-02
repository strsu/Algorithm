def solution(n, computers):
    answer = 0

    network = {}

    for i, computer in enumerate(computers):
        network[i] = []
        for j, c in enumerate(computer):
            if c:
                network[i].append(j)

    visited = []
    for com, net in network.items():
        if com not in visited:
            visited.append(com)
            answer += 1

            node = set(net)
            while node:
                n = node.pop()
                if n not in visited:
                    visited.append(n)

                    node = node | set(network[n])

    return answer


solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])


def solution(n, computers):
    answer = 0
    computer_id = list(range(1, len(computers) + 1))
    network = {}
    for i in range(n):
        network[i + 1] = [i + 1]

    for computer in computers:
        for i, c1 in enumerate(computer):
            for j, c2 in enumerate(computer[i + 1 :]):
                if i + j + 2 in network[i + 1]:
                    continue
                if c1 == c2 == 1 or i + j + 2 in network[i + 1]:
                    linked = network[i + 1]
                    linked.append(i + j + 2)
                    network[i + 1] = linked
                    linked = network[i + j + 2]
                    linked.append(i + 1)
                    network[i + j + 2] = linked
    for key, val in network.items():
        for v in val:
            if key == v:
                continue
            linked = network[v]
            network[v] = list(set(linked) | set(val))

    for key, val in network.items():
        if len(list(set(val) & set(computer_id))) > 0:
            computer_id = list(set(computer_id) - set(val))
            answer += 1

    return answer
