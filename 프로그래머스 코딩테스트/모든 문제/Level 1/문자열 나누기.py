# 문자열 나누기
def solution(s):
    # 초기값 설정
    answer = 0
    x = s[0]
    x_count = 1
    y_count = 0

    # 문자열 읽기
    for i in range(1, len(s)):

        # 초기값과 같은지 확인
        if x == s[i]:
            x_count += 1
        else:
            y_count += 1

        # x_count와 y_count가 같아지면 새로운 그룹으로 나눔
        if x_count == y_count:
            answer += 1
            if i + 1 < len(s):
                x = s[i + 1]  # 새로운 그룹의 첫 번째 문자로 갱신
            x_count = 0
            y_count = 0

    # 남은 문자열이 있을 경우 추가로 그룹 처리
    if x_count != y_count:
        answer += 1

    return answer

print(solution("aaabbaccccabba"))

# 두 번째 풀이 -> range를 쓰지 않고 푸는 방법

def solution2(s):
    answer = 0
    cnt1, cnt2 = 0, 0
    
    for i in s:
        if cnt1 == cnt2:
            answer += 1 # 남은 문자열 자동으로 처리
            cnt1, cnt2 = 0, 0
            x = i
        if i == x:
            cnt1 += 1
        else:
            cnt2 += 1
    
    return answer

print(solution2("aaabbaccccabba"))