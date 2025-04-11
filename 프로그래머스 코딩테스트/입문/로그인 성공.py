# 로그인 성공?
def solution(id_pw, db):
    id, pw = id_pw

    for db_id, db_pw in db:
        # 로그인 성공
        if db_id == id:
            if db_pw == pw:
                return "login"
            else:
                return "wrong pw"
    return "fail"

# 다른 사람 풀이1
def solution1(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"

# 다른 사람 풀이2
def solution2(id_pw, db):
    answer = "fail"
    for i in db:
        if i[0] == id_pw[0]:
            if i[1] == id_pw[1]:
                answer = "login"
            else:
                answer = "wrong pw"
            break
    return answer