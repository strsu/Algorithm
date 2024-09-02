import heapq

N, K = map(int, input().split())

purchase = 0
bottle = [[1, N]]
heapq.heapify(bottle)

while True:
    total_bottle = 0
    next_bottle = []
    # 합차기
    while bottle:
        l, n = heapq.heappop(bottle)
        print(l, n)

    if total_bottle <= K:
        break

    # bottle = next_bottle
    # 구매하기

    break

print(bottle)
