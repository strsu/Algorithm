D, K = map(int, input().split())
D -= 3

a = [0, 1]
b = [1, 1]

for _ in range(D):
    _a = a.pop(0)
    a.append(a[0] + _a)
    _b = b.pop(0)
    b.append(b[0] + _b)


num = 1
while True:
    if (K - (a[-1] * num)) % b[-1] == 0:
        print(num)
        print((K - (a[-1] * num)) // b[-1])
        break
    num += 1
