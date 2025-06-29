# 할 일 목록
def solution(todo_list, finished):
    answer = []
    true = True
    false = False
    for todo, finish in zip(todo_list, finished):
        if not finish:
            answer.append(todo)
    return answer

# 다른 사람 풀이1
def solution(todo_list, finished):
    return [work for idx, work in enumerate(todo_list) if not finished[idx]]

# 다른 사람 풀이2
def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        if finished[i]==False:
            answer.append(todo_list[i])
    return answer