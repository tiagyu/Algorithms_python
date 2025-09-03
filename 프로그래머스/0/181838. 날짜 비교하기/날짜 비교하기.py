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
        return 0
    else:
        return 1