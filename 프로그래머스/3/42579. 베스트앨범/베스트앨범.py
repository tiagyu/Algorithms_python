# 베스트앨범
def solution(genres, plays):
    
    answer = []
    genres_Dict1 = {}
    genres_Dict2 = {}
    
    for i, (g,p) in enumerate(zip(genres, plays)):
        if g not in genres_Dict1:
            genres_Dict1[g] = [(i, p)]
        else:
            genres_Dict1[g].append((i, p))
            
        if g not in genres_Dict2:
            genres_Dict2[g] = p
        else:
            genres_Dict2[g] += p
    
    for (k, v) in sorted(genres_Dict2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(genres_Dict1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
