# 컨트롤 제트
def solution(s):
    answer = 0
    s = s.split(" ")
    for i in range(len(s)):
        if s[i] == "Z":
            answer -= int(s[i-1])
        else:
            answer += int(s[i])
    return answer

# 다른 사람 풀이1
def solution2(s):
    stack = []
    for i in s.split():
        if i != "Z":
            stack.append(int(i))
        else:
            if stack:
                stack.pop()
    return sum(stack)

# 다른 사람 풀이 2
def solution3(s):
    arr = s.split(" ")
    result = []
    for i in arr:
        if i == "Z":
            result.pop()
        else:
            result.append(int(i))
    return sum(result)