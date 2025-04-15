# 이진수 더하기
def solution(bin1, bin2):
    bin_list = [2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**9, 2**10]

    bin1_split = list(map(int,bin1))
    bin2_split = list(map(int,bin2))

    bin1_split.reverse()
    bin2_split.reverse()

    bin1_value = 0
    bin2_value = 0

    for i in range(len(bin1)):
        bin1_value += bin_list[i] * bin1_split[i]

    for i in range(len(bin2)):
        bin2_value += bin_list[i] * bin2_split[i]

    answer = bin1_value + bin2_value
    return bin(answer)[2:]

# 다른 사람들 풀이1
def solution1(bin1, bin2):
    answer = bin(int(bin1, 2) + int(bin2, 2))[2:]
    return answer

# 다른 사람들 풀이2
def solution2(bin1, bin2):
    answer = 0
    bin1_size = len(bin1)
    bin2_size = len(bin2)
    
    sum = 0
    
    for i in bin1:
        sum += int(i) * (2 ** (bin1_size - 1))
        bin1_size -= 1
    
    for i in bin2:
        sum += int(i) * (2 ** (bin2_size - 1))
        bin2_size -= 1
        
    answer = str(bin(sum))[2:]
    return answer