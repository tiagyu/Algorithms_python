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