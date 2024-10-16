# 전화번호 목록

# solution 1 : 내가 푼 방식 -> 효율적 x
def solution(phone_book):
    # len 비교
    n = len(phone_book)
    
    # for문 생성
    for num in phone_book:
        for i in range(n):
            # 본인 제외
            if num == phone_book[i]:
                pass
            elif num == phone_book[i][:len(num)]:
                return False
            else:
                pass
    return True

print('Sol 1 :',solution(["12","123","1235","567","88"]))

# solution 2 : hash를 이용한 풀이 방식
def solution(phone_book): 

    # 1.Hash map생성
    hash_Dict = {} 
    for nums in phone_book: 
        hash_Dict[nums] = 1 
    
    # 2.접두어가 Hash map에 존재하는지 찾기 
    for nums in phone_book: 
        arr = "" 
        for num in nums: 
            arr += num
            # 3. 본인 자체일 경우는 제외
            if arr in hash_Dict and arr != nums:       
                return False 
                
    return True

print('Sol 2 :',solution(["119", "97674223", "1195524421"]))

def solution3(phoneBook):
    
    # 숫자별로 정렬
    phoneBook.sort()

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

print('Sol 3 :',solution3(["119", "97674223", "1195524421"]))
