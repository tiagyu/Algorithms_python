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