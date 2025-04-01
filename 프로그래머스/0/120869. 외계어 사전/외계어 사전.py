def solution(spell, dic):
    answer = 0
    sort_spell = sorted(spell)

    for i in dic:
        sort_dic = sorted(i)
        if sort_dic == sort_spell:
            answer = 1
            break
        else:
            answer = 2
    return answer