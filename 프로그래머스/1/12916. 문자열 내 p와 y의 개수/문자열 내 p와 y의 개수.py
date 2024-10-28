def solution(s):
    
    # 모두 소문자로 변환
    s_low = s.lower()
    p_count = 0
    y_count = 0
    
    for i in s_low:
        if i == 'p':
            p_count += 1
        elif i == 'y':
            y_count += 1
    
    if p_count == y_count:
        return True
    else:
        return False