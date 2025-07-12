def solution(phone_number):
    last_number = phone_number[-4:]
    answer = (len(phone_number)-4) * "*" + last_number
    return answer