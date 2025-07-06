# [1차] 비밀지도
def solution(n, arr1, arr2):
    binary_num_arr1, binary_num_arr2,arr,answer = [], [], [],[]

    for i in range(n):
        binary_num_arr1.append(list(str(format(arr1[i],f"0{n}b"))))
        binary_num_arr2.append(list(str(format(arr2[i],f"0{n}b"))))
        for j in range(n):
            arr.append(int(binary_num_arr1[i][j]) + int(binary_num_arr2[i][j]))
        
    result = ['#' if numb > 0 else " " for numb in arr]
    for i in range(0,len(result),n):
        answer.append("".join(result[i:i+n]))
    return answer

# 다른 사람 풀이1
def solution1(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

# 다른 사람 풀이2
def solution2(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = str(bin(arr1[i]|arr2[i])[2:]).rjust(n,'0').replace('1','#').replace('0',' ')
        answer.append(a)
    return answer