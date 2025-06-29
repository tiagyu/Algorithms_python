def solution(todo_list, finished):
    answer = []
    true = True
    false = False
    for todo, finish in zip(todo_list, finished):
        if not finish:
            answer.append(todo)
    return answer