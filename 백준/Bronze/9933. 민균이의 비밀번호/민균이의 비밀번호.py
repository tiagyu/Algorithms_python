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