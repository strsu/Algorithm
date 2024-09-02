def solution(book_time):
    answer = []

    book_time = sorted(book_time, key=lambda x: x[0])

    for t in book_time:
        s, e = t
        s = 60 * int(s.split(":")[0]) + int(s.split(":")[1])
        e = 60 * int(e.split(":")[0]) + int(e.split(":")[1])

        if not answer:
            # 최초 시작
            answer.append(e)
            continue

        is_need_room = True
        for i, v in enumerate(answer):
            if v + 10 <= s:
                answer[i] = e
                is_need_room = False
                break
        if is_need_room:
            answer.append(e)

    return len(answer)


book_time = [
    ["15:00", "17:00"],
    ["16:40", "18:20"],
    ["14:20", "15:20"],
    ["14:10", "19:20"],
    ["18:20", "21:20"],
]
book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
solution(book_time)
