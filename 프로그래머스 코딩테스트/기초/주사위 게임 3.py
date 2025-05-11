# 주사위 게임 3
def solution(a, b, c, d):
    values = [a, b, c, d]
    count_dict= {}

    for v in values:
        count_dict[v] = count_dict.get(v,0) + 1
    
    
    # 4개가 같은 경우 -> 1111 × p
    if len(count_dict) == 1:
        return 1111 * v

    # 3개가 같은 경우 -> (10 × p + q)**2
    elif len(count_dict) == 2:
        keys = list(count_dict.keys())
        vals = list(count_dict.values())
        
        if 3 in vals:
            p = keys[vals.index(3)]
            q = keys[vals.index(1)]
            return (10 * p + q) ** 2
        # 2개가 같은 경우1 -> 2개씩 같은 값 -> (p + q) × |p - q|
        else:
            p,q = keys
            return (p + q) * abs(p - q)

    elif len(count_dict) == 3:
        # 2개가 같은 경우2 -> q × r
        p = 0
        qr_list = []
        
        for k,v in count_dict.items():
            if v == 2:
                p = k
            elif v == 1:
                qr_list.append(k)
        
        q,r = qr_list
        return q * r

    # 하나도 같지 않은 경우 -> 최소 값
    else:
        return min(count_dict.keys())
    
# 다른 사람 풀이1
def solution1(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 2:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)
    
# 다른 사람 풀이2
def solution2(a, b, c, d):
    dice = [a,b,c,d]
    dice.sort()
    a, b, c, d = dice
    s = set(dice)
    if len(s) == 1:
        return 1111*a
    elif len(s) == 4:
        return min(a,b,c,d)
    elif len(s) == 2:
        if a==b==c:
            return (10*a+d)**2
        elif b==c==d:
            return (10*b+a)**2
        else:
            return (b+c)*(abs(b-c))
    else:
        if a == b: 
            return c*d
        elif b == c:
            return a*d
        else:
            return a*b