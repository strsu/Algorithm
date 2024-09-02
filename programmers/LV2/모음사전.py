def solution(word):
    answer = 1
    now = ["1"]
    word = (
        word.replace("A", "1")
        .replace("E", "2")
        .replace("I", "3")
        .replace("O", "4")
        .replace("U", "5")
    )

    while "".join(now) != word:
        if len(now) < 5:
            now.append("1")
        else:
            if now[4] == "5":
                idx = 3
                while True:
                    if now[idx] != "5":
                        now = now[:idx] + [str(int(now[idx]) + 1)]
                        break
                    else:
                        idx -= 1
            else:
                now = now[:4] + [str(int(now[4]) + 1)]

        answer += 1

    return answer


solution("EIO")
