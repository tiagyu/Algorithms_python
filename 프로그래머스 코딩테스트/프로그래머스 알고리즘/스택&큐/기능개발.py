# 기능 개발
# solution 1 내 풀이
def solution(progresses, speeds):
    # 남은 작업 기간 계산
    days = []
    for p,s in zip(progresses, speeds):
        last_days = (100-p)
        # 남은 일수 올림
        if last_days % s == 0:
            days.append(last_days // s)
        else:
            days.append((last_days // s) + 1)
    
    result = []
    # 첫 번째 기능의 배포 일자를 기준으로 설정
    current_day = days[0]
    count = 1
    
    # 각 기능의 배포 일자 비교
    for i in range(1, len(days)):
        if days[i] <= current_day:
            # 현재 배포 일자보다 뒤의 기능이 먼저 끝나면 같이 배포
            count+=1
        else:
            # 새로 배포 일자를 갱신하고 결과에 추가
            result.append(count)
            current_day = days[i]
            count = 1
            
    # 마지막 남은 기능들의 배포 수 추가
    result.append(count)
            
    return result

print(solution([93, 30, 55],[1, 30, 5]))

# solution2 pop 이용
def solution2(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len (progresses) > 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    
    return answer

print(solution2([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))

# solution3 2차원 배열
def solution3(progresses, speeds):
    q = []
    for p,s in zip(progresses, speeds):
        if len(q) == 0 or q[-1][0] < -((p-100)//s):
            q.append([-((p-100)//s),1])
        else:
            q[-1][1] += 1
    return [i[1] for i in q]

print(solution3([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))