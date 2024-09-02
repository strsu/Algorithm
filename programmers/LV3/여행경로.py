from collections import defaultdict


def solution(tickets):
    ticket_dict = defaultdict(list)
    answer = ["ICN"]

    for s, d in tickets:
        ticket_dict[s].append(d)

    for key in ticket_dict.keys():
        ticket_dict[key].sort(reverse=True)

    while len(answer) < len(tickets) + 1:
        now = answer[-1]

        # 티켓을 다 안 썼는데, 경로가 없으면 롤백
        if now not in ticket_dict or not ticket_dict[now]:
            while True:
                now = answer.pop()
                prev = answer[-1]
                ticket_dict[prev].insert(0, now)
                if len(ticket_dict[prev]) > 1:
                    break
        else:
            next = ticket_dict[now].pop()
            answer.append(next)

    # print(answer)
    return answer


# solution(
#     [
#         ["ICN", "BOO"],  #
#         ["ICN", "COO"],  #
#         ["BOO", "DOO"],  #
#         ["BOO", "ICN"],  #
#         ["COO", "BOO"],
#         ["COO", "DOO"],  #
#         ["DOO", "COO"],
#         ["DOO", "BOO"],  #
#     ]
# )
# solution(
#     [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
# )


# solution(
#     [
#         ["ICN", "BOO"],
#         ["ICN", "COO"],
#         ["COO", "DOO"],
#         ["DOO", "COO"],
#         ["BOO", "DOO"],
#         ["DOO", "BOO"],
#         ["BOO", "ICN"],
#         ["COO", "BOO"],
#     ]
# )
# solution(
#     [
#         ["ICN", "BOO"],
#         ["BOO", "COO"],
#         ["COO", "ICN"],
#         ["ICN", "BOO"],
#         ["BOO", "COO"],
#         ["COO", "ICN"],
#     ]
# )
# solution(
#     [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
# )
# print("ASDf")
# solution(
#     [
#         ["ICN", "JFK"], #
#         ["JFK", "AAA"]
#         ["AAA", "HND"],
#         ["HND", "IAD"],
#         ["JFK", "HND"],

#     ]
# )
# solution(
#     [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
# )
solution(
    [
        ["ICN", "BBB"],
        ["BBB", "CCC"],
        ["CCC", "ICN"],
        ["ICN", "AAA"],
        ["AAA", "DDD"],
        ["DDD", "EEE"],
    ]
)
