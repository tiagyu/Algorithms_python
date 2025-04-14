# 문자열 붙여서 출력하기
str1, str2 = input().strip().split(' ')
answer = "".join([str1,str2])
print(answer)

# 다른 사람 풀이1
print(input().strip().replace(" ",""))

# 다른 사람 풀이2
str1, str2 = input().strip().split(' ')
print(str1,str2,sep="")