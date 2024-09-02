BOARD = input()

BOARD = BOARD.replace("XXXX", "AAAA").replace("XX", "BB")

if "X" in BOARD:
    print(-1)
else:
    print(BOARD)
