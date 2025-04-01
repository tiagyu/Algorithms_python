# 외계어 사전
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

# 다른 사람 풀이1
def solution1(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell - set(s):
            return 1
    return 2

# 다른 사람 풀이2
def solution2(spell, dic):
    for d in dic:
        if sorted(dic) == sorted(spell):
            return 1
    return 2