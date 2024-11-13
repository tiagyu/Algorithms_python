# 25497 : 기술 연계마스터 임스
N = int(input())
skill = input()
count = 0
Ls, Ss = 0, 0  # 사전 기술 'L'과 'S'의 사용 가능 횟수

for i in skill:
    if '0' <= i <= '9':  # 독립적인 숫자 기술
        count += 1
    elif i == 'L':  # 사전 기술 L
        Ls += 1
    elif i == 'R':  # 본 기술 R
        if Ls > 0:  # L이 먼저 사용된 경우
            count += 1
            Ls -= 1  # 사용한 L의 횟수 감소
        else:
            break  # L이 없으면 이후 모든 기술 무효화
    elif i == 'S':  # 사전 기술 S
        Ss += 1
    elif i == 'K':  # 본 기술 K
        if Ss > 0:  # S가 먼저 사용된 경우
            count += 1
            Ss -= 1  # 사용한 S의 횟수 감소
        else:
            break  # S가 없으면 이후 모든 기술 무효화

print(count)

