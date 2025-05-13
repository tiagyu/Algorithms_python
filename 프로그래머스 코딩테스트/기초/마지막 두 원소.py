# 마지막 두 원소
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1]-num_list[-2])
    else:
        num_list.append(num_list[-1] *2)
    return num_list

# 다른 사람 풀이1
def solution1(l):
    l.append(l[-1]-l[-2] if l[-1]>l[-2] else l[-1]*2)
    return l

# 다른 사람 풀이2
def solution2(num_list):
    a=num_list[-1]
    b=num_list[-2]
    if a>b:num_list.append(a-b)
    else: num_list.append(2*a)
    return num_list