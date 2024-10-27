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