def solution(babbling):
    answer = 0
    babbling_list = [
    'aya',"ye",'woo',"ma"
    ]

    for i in babbling:
        for j in babbling_list:
            # aya case
            if i.count(j) == 1:
                i = i.split(j)
                i = ",".join(i)
        i = i.replace(",","")
        if len(i) == 0:
            answer += 1
    return answer
