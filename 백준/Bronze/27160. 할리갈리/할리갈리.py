# 할리갈리
N = int(input())
hashDict = {}

cards = [input().split() for _ in range(N)]

for i in cards:
    if i[0] in hashDict:
        hashDict[i[0]] += int(i[1])
    else:
        hashDict[i[0]] = int(i[1])

# found = False

# for value in hashDict.values():
#     if value == 5:
#         print('YES')
#         found = True
#         break
    
# if not found:
#     print('No')

check = 5 in hashDict.values()	# 5개 있는지 확인

if check : print('YES')
else : print('NO')