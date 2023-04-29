def solution(board):

    O_cnt = "".join(board).count("O")
    X_cnt = "".join(board).count("X")

    if O_cnt - X_cnt not in (0, 1):
        # X가 더 많을 수 없다.
        # O가 X보다 2개 이상 많을 수 없다.
        return 0

    if O_cnt == X_cnt:
        # O와 X의 갯수가 같다면
        # O로 인해 게임이 끝나는 모형이 나올 수 없다.

        # 가로 검사
        for b in board:
            if b.count("O") == 3:
                return 0
        # 세로 검사
        for b in zip(*board):
            if b.count("O") == 3:
                return 0

        # 대각선 검사
        if (
            board[0][0] == board[1][1] == board[2][2] == "O"
            or board[0][2] == board[1][1] == board[2][0] == "O"
        ):
            return 0

        return 1

    # 가로 검사
    for b in board:
        if b.count("X") == 3:
            return 0
    # 세로 검사
    for b in zip(*board):
        if b.count("X") == 3:
            return 0

    # 대각선 검사
    if (
        board[0][0] == board[1][1] == board[2][2] == "X"
        or board[0][2] == board[1][1] == board[2][0] == "X"
    ):
        return 0

    return 1
