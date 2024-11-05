# 민규이의 비밀번호
# 내 풀이
N = int(input())
passwords = []
hash_Dict = {}
for _ in range(N):
    passwords.append(input())

for i in passwords:
    if i[::-1] in passwords:
        hash_Dict[len(i)] = i[len(i)//2]

for key, value in hash_Dict.items():
    print(key, value)

# 다른 사람의 풀이

import sys
input = sys.stdin.readline

N = int(input())
files = [input().rstrip() for _ in range(N)]

for i in range(N-1):
    for j in range(i,N):
        if files[i][::-1] == files[j]:
            print(len(files[i]), files[i][len(files[i])//2])
            exit()