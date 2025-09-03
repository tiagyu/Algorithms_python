# 날짜 비교하기
def solution(date1, date2):
    year = date1[0] - date2[0]
    month = date1[1] - date2[1]
    day = date1[2] - date2[2]

    if year == 0:
        if month == 0:
            if day == 0:
                return 0
            elif day > 0:
                return 0
            else:
                return 1
        elif month > 0:
            return 0
        else:
            return 1
    elif year > 0:
        return 1
    else:
        return 0


# 다른 사람 풀이1
def solution1(date1, date2):
    return int(date1 < date2)


# 다른 사람 풀이2
def solution(date1, date2):
    for i in range(3):
        if date1[i] < date2[i]:
            return 1
        elif date2[i] < date1[i]:
            return 0
    return 0
