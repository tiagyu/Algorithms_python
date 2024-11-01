# 올바른 괄호
# solution 1 
def solution(s):
    count = 0
    
    for i in s:
        if i == '(' :
            count += 1
        else:
            count -= 1
            if count < 0 :
                return False
    
    return count == 0

print(solution(")()("))

# solution 2
def solution1(s):
    s_list = list()
    for c in s:
        if c == '(' :
            s_list.append(c)
        
        if c == ')' :
            try:
                s_list.pop()
            except IndexError:
                return False
    
    return len(s_list) == 0

print(solution1("(())()"))