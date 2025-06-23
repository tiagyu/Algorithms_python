# 왼쪽 오른쪽
def solution(str_list):
    if 'l' in str_list and 'r' in str_list:
        l_index = str_list.index('l')
        r_index = str_list.index('r')
        if l_index < r_index:
            return str_list[:l_index]
        elif l_index > r_index:
            return str_list[r_index+1:]
    elif 'l' in str_list:
        return str_list[:str_list.index('l')]
    elif 'r' in str_list:
        return str_list[str_list.index('r')+1:]
    else:
        return []

# 다른 사람 풀이1
def solution1(str_list):
    for i in range(len(str_list)):
        if str_list[i]=='l': return str_list[:i]
        elif str_list[i]=='r': return str_list[i+1:]
    return []

# 다른 사람 풀이2
def solution2(str_list):
    for i, s in enumerate(str_list):
        if s == 'l':
            return str_list[:i]
        elif s == 'r':
            return str_list[i+1:]
    return []